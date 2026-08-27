# File Organizer

A simple Python script that organizes files in a folder — sorting them into subfolders based on file extension.

## What it does

- Iterates through all files in the given folder
- Checks each file's extension (e.g. `.jpg`, `.pdf`, `.txt`)
- Creates a subfolder named after the extension (if it doesn't exist) and moves the file there
- Files with no extension are moved to a `no_extension` folder

## Requirements

- Python 3.x (uses only built-in modules: `os`, `sys`, `shutil`)

## Usage

python organizer.py <folder_path>

## Example:

python organizer.py C:\Users\user\Downloads

## Example

Folder before running:
Downloads/
photo.jpg
report.pdf
notes.txt
Makefile


Folder after running:
Downloads/
.jpg/photo.jpg
.pdf/report.pdf
.txt/notes.txt
no_extension/Makefile


## Author

Kacper Kaleta