import os 
import shutil

def move_files_by_type(source_dir, dest_dir, file_extension):
    for filename in os.listdir(source_dir):
        if filename.endswith(file_extension):
            shutil.move(os.path.join(source_dir, filename), os.path.join(dest_dir, filename))


move_files_by_type('/path/to/source', '/path/to/destination', '.pdf')
