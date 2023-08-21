import os
import hashlib
import shutil
from tqdm import tqdm

def get_file_hash(file_path, block_size=65536):
    """
    Computes the SHA-1 hash of the provided file.

    Args:
    - file_path (str): Path to the file to be hashed.
    - block_size (int, optional): Size of the block to read from the file while hashing. Default is 65536 bytes.

    Returns:
    - str: Hexadecimal representation of the hash or None in case of an error.
    """
    sha1 = hashlib.sha1()
    try:
        with open(file_path, 'rb') as f:
            for block in iter(lambda: f.read(block_size), b''):
                sha1.update(block)
        return sha1.hexdigest()
    except Exception as e:
        print(f"Error hashing file {file_path}: {e}")
        return None

def copy_files(source_directory, dest_directory, min_size_kb=12):
    """
    Processes and organizes the files from source_directory to dest_directory.

    Args:
    - source_directory (str): Path to the source directory containing the files to be processed.
    - dest_directory (str): Path to the destination directory where organized files will be saved.
    - min_size_kb (int, optional): Minimum size (in KB) of files that should be considered. Default is 12KB.
    """
    processed_files = set()
    hash_list = {}

    for root, _, files in os.walk(source_directory):
        for file in tqdm(files, desc="Processing files"):
            full_path = os.path.join(root, file)
            file_size = os.path.getsize(full_path) / 1024  # size in KB

            if file_size > min_size_kb:
                file_extension = os.path.splitext(file)[1].lstrip('.').lower()

                if not file_extension:
                    file_extension = "unknown"

                dest_subfolder = os.path.join(dest_directory, file_extension)
                dest_path = os.path.join(dest_subfolder, file)

                # Create the destination subfolder if it doesn't exist
                os.makedirs(dest_subfolder, exist_ok=True)

                # If the file has a potential duplicate
                if file_size in processed_files:
                    # If the hash is not in hash_list, compute and store it
                    if full_path not in hash_list:
                        hash_list[full_path] = get_file_hash(full_path)

                    # Check if this hash already exists in destination folder
                    is_duplicate = False
                    for other_path, other_hash in hash_list.items():
                        if other_hash == hash_list[full_path] and other_path != full_path:
                            is_duplicate = True
                            break

                    if not is_duplicate:
                        shutil.copy2(full_path, dest_path)

                else:
                    shutil.copy2(full_path, dest_path)
                    processed_files.add(file_size)

    print("File processing completed.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python handler.py <source_directory> <dest_directory> [min_size_kb]")
        sys.exit(1)

    source_directory = sys.argv[1]
    dest_directory = sys.argv[2]
    min_size_kb = int(sys.argv[3]) if len(sys.argv) > 3 else 12

    copy_files(source_directory, dest_directory, min_size_kb)
