# File Handler

The File Handler is a utility designed to organize files, deduplicate based on SHA-1 hashing, and move them to appropriate directories based on their extensions. It provides a progress bar for a visual representation during the file processing phase.

## Installation

1. Clone this repository:
   ```bash
   git clone [Your Repository URL]
   cd [Your Repository Name]

    Run the installation script to set up the virtual environment and install the required dependencies:

    For Linux/macOS:

    bash

python install.py

For Windows:

batch

    python install.py

Usage

    Navigate to the directory containing the handler scripts.

    Execute the starting script:

    For Linux/macOS:

    bash

    ./start.sh

    For Windows:
    Double-click start.bat or run it from the command prompt.

    Follow the prompts to specify the source directory, destination directory, and the desired file extension.

Features

    Organization: Organizes files into directories based on their extensions.

    Deduplication: Identifies potential duplicate files based on size, and then by content using SHA-1 hashing to ensure that the same file doesn't get moved multiple times.

    Progress Bar: A visual representation of the processing phase, ensuring that users can track the progress of the script's operations.

Functions
get_file_hash(file_path, block_size=65536)

Computes the SHA-1 hash of the provided file.

    file_path: Path to the file to be hashed.
    block_size: Size of the block to read from the file while hashing. Default is 65536 bytes.

Returns the hexadecimal representation of the hash.
copy_files(source_directory, dest_directory, min_size_kb=12)

Processes and organizes the files from the source directory to the destination directory.

    source_directory: Path to the source directory containing the files to be processed.
    dest_directory: Path to the destination directory where organized files will be saved.
    min_size_kb: Minimum size (in KB) of files that should be considered. Default is 12KB.

Processes the files, organizes them based on extensions, and checks for duplicates.
Contributing

If you're interested in contributing to the project, please submit a pull request or open an issue for discussion.
