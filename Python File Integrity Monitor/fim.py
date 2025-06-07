import hashlib
import os
import time

def calculate_file_hash(file_path):
    hash_object = hashlib.sha256()
    with open(file_path, 'rb') as file:
        file_data = file.read()
        hash_object.update(file_data)
    return hash_object.hexdigest()

def log_change(file_path):
    log_directory = 'logs'
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
    log_file_path = os.path.join(log_directory, 'file_changes.log')
    with open(log_file_path, 'a') as log_file:
        log_file.write(f"{time.ctime()}: {file_path} has changed.\n")

def monitor_files():
    files_to_monitor = ['watched_file.txt']
    previous_hashes = {}

    while True:
        for file_path in files_to_monitor:
            if os.path.exists(file_path):
                current_hash = calculate_file_hash(file_path)
                if file_path not in previous_hashes:
                    previous_hashes[file_path] = current_hash
                elif previous_hashes[file_path] != current_hash:
                    print(f"File has changed: {file_path}")
                    log_change(file_path)
                    previous_hashes[file_path] = current_hash
                else:
                    print(f"No change detected for {file_path}")
            else:
                print(f"File does not exist: {file_path}")
        time.sleep(5)

if __name__ == "__main__":
    monitor_files()