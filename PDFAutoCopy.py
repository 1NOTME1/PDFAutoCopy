import os
import shutil
import time

source_folder = r'...'
destination_folder = r'...'
copied_files = set()

while True:
    for filename in os.listdir(source_folder):
        if filename.endswith('.pdf') and filename not in copied_files:
            source_file = os.path.join(source_folder, filename)
            destination_file = os.path.join(destination_folder, filename)
            shutil.copy(source_file, destination_file)
            copied_files.add(filename)
            print(f'Copied: {filename}')
    time.sleep(3)
