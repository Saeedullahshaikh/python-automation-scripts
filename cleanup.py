import os
import time

def cleanup_old_files(directory, days_old):
    current_time = time.time()

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_age = current_time - os.path.getmtime(file_path)
            if file_age > days_old * 86400:
                os.remove(file_path)
                print(f"deleted: {filename}")

#example
cleanup_old_files('', 30) #deleted files older than 30 days