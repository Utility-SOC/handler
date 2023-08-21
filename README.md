#Overview

#The handler.py script provides functionalities to filter, deduplicate, and organize files based on their extensions. This script works in tandem with an installation script (install.py) and a launcher batch #file (launch.bat) to ensure smooth operation.
#Table of Contents

    System Requirements
    Installation Instructions
    Usage Instructions
    Functional Overview
    Function Definitions

#1. System Requirements:

#    Python 3.6 or higher
#    Windows, macOS, or Linux operating system

#2. Installation Instructions:

#    Clone the repository or download the script files.
#    Navigate to the directory containing install.py.
#    Execute install.py:

#python install.py

#This will set up a Python virtual environment and install the required dependencies.
#3. Usage Instructions:

#    Use the launch.bat file to start the script.
#    When prompted, provide the source folder, destination folder, and desired file extension (or press Enter for all files).
#    The script will process the files and provide feedback on its operations.

#4. Functional Overview:

#    Filter Files: Only considers files that are larger than 12KB. Ignores 0KB files and files smaller than 12KB.
#    Deduplication: Checks for potential duplicates based on file size first. If there are multiple files with the same size and similar filenames (e.g., a.jpg and a 1.jpg), the script will hash the files to check for content similarity. Duplicate files (by content) will be ignored.
#    Organize Files: Files will be moved into subfolders named according to their file extensions.

#5. Function Definitions:
#get_file_hash(file_path, block_size=65536)

#This function computes the SHA1 hash of the provided file.
#Parameters:

#    file_path: Path to the file to be hashed.
#    block_size: Size of the block to read from the file while hashing. Default is 65536 bytes.

#Returns:

#    String (hexadecimal representation of the hash) or None in case of an error.

#copy_files(source_directory, dest_directory, min_size_kb)

#Main driver function that processes and organizes the files.
#Parameters:

#    source_directory: Path to the source directory containing the files to be processed.
#    dest_directory: Path to the destination directory where organized files will be saved.
#    min_size_kb: Minimum size (in KB) of files that should be considered.
