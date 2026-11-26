
# Personal File Backup Manager

A Python application for creating, managing, searching, and restoring backups of important files and folders.

## Features

- Create file backups.
- Create folder backups.
- Generate unique backup IDs.
- Store backup history in JSON.
- View all backup records.
- Search backups.
- Restore files and folders.
- Delete unwanted backups.
- Prevent overwriting existing restore destinations.
- Automatically create backup directories.

## Technologies Used

- Python
- JSON
- File Handling
- shutil
- pathlib
- Object-Oriented Programming

## Project Structure

```text
Personal_File_Backup_Manager/
│
├── main.py
├── backup_manager.py
├── history_manager.py
├── backups/
│   └── .gitkeep
├── backup_history.json
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/Personal_File_Backup_Manager.git
```

### 2. Open the folder

```bash
cd Day396_Personal_File_Backup_Manager
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

Activate on Windows:

```bash
venv\Scripts\activate
```

### 4. Run the application

```bash
python main.py
```

No external packages are required.

## How to Use

1. Select Create Backup.
2. Enter the complete file or folder path.
3. View Backup History to find the generated backup ID.
4. Select Restore Backup and enter the ID.
5. Enter a new destination path.
6. Search or delete backups when needed.

## Example

```text
PERSONAL FILE BACKUP MANAGER

1. Create Backup
2. View Backup History
3. Restore Backup
4. Search Backups
5. Delete Backup
6. Exit
```

## Learning Objectives

- Understand Python file handling.
- Work with JSON data storage.
- Use shutil for copying files and folders.
- Use pathlib for path management.
- Implement CRUD operations.
- Understand exception handling.
- Practice Object-Oriented Programming.

## Future Improvements

- Automatic scheduled backups.
- Backup compression using ZIP.
- Password-protected backups.
- Backup progress indicator.
- Duplicate file detection.
- Graphical interface using Tkinter.

## Author

Python Developer

## License

Created for educational and learning purposes.
