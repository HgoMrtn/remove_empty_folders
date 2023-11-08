# Folder Cleaning

This Python script deletes all empty folders and subfolders in the directory where the script is executed. It serves as a convenient tool to clean up unused directories and optimize folder structures. The script also generates a log file containing the paths of the deleted empty folders for reference.

## How to Use
- Place the script in the folder you want to clean.
- Execute the script.
- The deleted folders are saved to a text file named `deleted_directories_log.txt` created by the script.

## Inspiration
This script was inspired by the solution provided on [Stack Overflow](https://stackoverflow.com/questions/22001216/scan-files-recursively-and-delete-empty-directories-in-python).

## Script Execution
```bash
python remove_empty_folders.py
```

## Script Explanation

1. **Scanning Directories:**
   - The script starts by scanning the current directory and its subdirectories using `os.walk()`.
  
2. **Identifying Empty Directories:**
   - It identifies empty directories by checking if a directory has no subdirectories and no files.
  
3. **Deleting Empty Directories:**
   - Empty directories are deleted using `os.rmdir()` function.
  
4. **Logging Used Directories:**
   - Directories with subdirectories or files are logged into the `deleted_directories_log.txt` file.
  
5. **Summary in Log File:**
   - The log file provides a summary of the cleaning process, including paths of deleted empty folders and counts of empty and used directories.

The script provides a convenient way to remove unused directories, optimizing folder structures and enhancing overall organization. It also offers transparency by logging deleted empty folders for reference.

⚠️ Don't execute this code if you don't understand it!
