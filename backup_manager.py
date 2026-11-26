import os
import shutil
import uuid
from datetime import datetime
from pathlib import Path

from history_manager import load_history, save_history


class BackupManager:

    def __init__(self):
        self.backup_folder = Path("backups")
        self.backup_folder.mkdir(exist_ok=True)
        self.history = load_history()

    def create_backup(self, source_path):
        source = Path(source_path).expanduser().resolve()

        if not source.exists():
            print("\nSource path does not exist.")
            return

        if not source.is_file() and not source.is_dir():
            print("\nUnsupported source type.")
            return

        backup_id = str(uuid.uuid4())[:8]
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        backup_name = f"{source.name}_{timestamp}_{backup_id}"
        destination = self.backup_folder / backup_name

        try:
            if source.is_file():
                shutil.copy2(source, destination)
                backup_type = "File"
            else:
                shutil.copytree(source, destination)
                backup_type = "Folder"

            record = {
                "id": backup_id,
                "source": str(source),
                "backup_path": str(destination),
                "type": backup_type,
                "created_at": datetime.now().strftime(
                    "%Y-%m-%d %H:%M:%S"
                )
            }

            self.history.append(record)
            save_history(self.history)

            print("\nBackup created successfully!")
            print(f"Backup ID: {backup_id}")
            print(f"Location: {destination}")

        except (OSError, shutil.Error) as error:
            print(f"\nBackup failed: {error}")

            if destination.exists():
                if destination.is_dir():
                    shutil.rmtree(destination)
                else:
                    destination.unlink()

    def view_backups(self):
        if not self.history:
            print("\nNo backup records found.")
            return

        print("\n========== BACKUP HISTORY ==========")

        for record in self.history:
            print("\n" + "-" * 45)
            print(f"ID         : {record['id']}")
            print(f"Source     : {record['source']}")
            print(f"Backup     : {record['backup_path']}")
            print(f"Type       : {record['type']}")
            print(f"Created At : {record['created_at']}")

            if not Path(record["backup_path"]).exists():
                print("Status     : Missing")
            else:
                print("Status     : Available")

    def find_backup(self, backup_id):
        for record in self.history:
            if record["id"] == backup_id:
                return record

        return None

    def restore_backup(self, backup_id, restore_path):
        record = self.find_backup(backup_id)

        if not record:
            print("\nBackup ID not found.")
            return

        backup_path = Path(record["backup_path"])
        destination = Path(restore_path).expanduser().resolve()

        if not backup_path.exists():
            print("\nBackup file or folder is missing.")
            return

        if destination.exists():
            print("\nDestination already exists.")
            print("Choose a new destination to avoid overwriting.")
            return

        try:
            destination.parent.mkdir(parents=True, exist_ok=True)

            if backup_path.is_file():
                shutil.copy2(backup_path, destination)
            else:
                shutil.copytree(backup_path, destination)

            print("\nBackup restored successfully!")
            print(f"Restored location: {destination}")

        except (OSError, shutil.Error) as error:
            print(f"\nRestore failed: {error}")

    def search_backups(self, keyword):
        keyword = keyword.lower()

        results = [
            record for record in self.history
            if keyword in record["source"].lower()
            or keyword in record["type"].lower()
            or keyword in record["id"].lower()
        ]

        if not results:
            print("\nNo matching backups found.")
            return

        print("\n========== SEARCH RESULTS ==========")

        for record in results:
            print(
                f"\nID: {record['id']}"
                f"\nSource: {record['source']}"
                f"\nType: {record['type']}"
                f"\nCreated: {record['created_at']}"
            )

    def delete_backup(self, backup_id):
        record = self.find_backup(backup_id)

        if not record:
            print("\nBackup ID not found.")
            return

        backup_path = Path(record["backup_path"])

        try:
            if backup_path.is_dir():
                shutil.rmtree(backup_path)
            elif backup_path.exists():
                backup_path.unlink()

            self.history.remove(record)
            save_history(self.history)

            print("\nBackup deleted successfully!")

        except OSError as error:
            print(f"\nUnable to delete backup: {error}")
