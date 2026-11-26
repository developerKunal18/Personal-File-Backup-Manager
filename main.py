from backup_manager import BackupManager

manager = BackupManager()


def create_backup():
    print("\n========== CREATE BACKUP ==========")
    source = input("Enter file or folder path: ").strip()

    if source:
        manager.create_backup(source)
    else:
        print("Path cannot be empty.")


def restore_backup():
    print("\n========== RESTORE BACKUP ==========")

    backup_id = input("Enter backup ID: ").strip()
    restore_path = input("Enter destination path: ").strip()

    if backup_id and restore_path:
        manager.restore_backup(backup_id, restore_path)
    else:
        print("Backup ID and destination are required.")


def search_backup():
    keyword = input("\nEnter ID, file name, or type: ").strip()

    if keyword:
        manager.search_backups(keyword)
    else:
        print("Search keyword cannot be empty.")


def delete_backup():
    backup_id = input("\nEnter backup ID to delete: ").strip()

    if not backup_id:
        print("Backup ID cannot be empty.")
        return

    confirmation = input(
        "Are you sure you want to delete this backup? (yes/no): "
    ).strip().lower()

    if confirmation == "yes":
        manager.delete_backup(backup_id)
    else:
        print("Deletion cancelled.")


def main():
    while True:
        print("\n" + "=" * 45)
        print("       PERSONAL FILE BACKUP MANAGER")
        print("=" * 45)

        print("1. Create Backup")
        print("2. View Backup History")
        print("3. Restore Backup")
        print("4. Search Backups")
        print("5. Delete Backup")
        print("6. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            create_backup()

        elif choice == "2":
            manager.view_backups()

        elif choice == "3":
            restore_backup()

        elif choice == "4":
            search_backup()

        elif choice == "5":
            delete_backup()

        elif choice == "6":
            print("\nThank you for using Backup Manager!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()
