#!/bin/bash

# Activate the virtual environment
source venv/bin/activate

# Prompt for the source and destination directories and the file extension
echo "Enter the source directory:"
read source_directory

echo "Enter the destination directory:"
read dest_directory

echo "Enter desired file extension (press Enter for all files):"
read file_extension

if [[ -z "$file_extension" ]]; then
    python handler.py "$source_directory" "$dest_directory"
else
    python handler.py "$source_directory" "$dest_directory" "$file_extension"
fi

# Deactivate the virtual environment
deactivate
