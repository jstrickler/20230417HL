import os
from datetime import datetime
import sys


FOLDER_NAME = "DATA"
FILE_NAME = "alice.txt"

file_path = os.path.join(FOLDER_NAME, FILE_NAME)
print(f"file_path: {file_path}")

file_name = os.path.basename(file_path)
folder = os.path.dirname(file_path)
abs_path = os.path.abspath(file_path)
print(f"file_name: {file_name}")
print(f"folder: {folder}")
print(f"abs_path: {abs_path}")
print(f"os.path.splitext(file_path): {os.path.splitext(file_path)}")
file_size = os.path.getsize(file_path)
print(f"file_size: {file_size}")
raw_timestamp = os.path.getmtime(file_path)
print(f"raw_timestamp: {raw_timestamp}")
file_mod_time = datetime.fromtimestamp(raw_timestamp)
print(f"file_mod_time: {file_mod_time}")
print()

for thing in FILE_NAME, FOLDER_NAME, file_path, "wombats.txt":
    print(f"{thing:20s} {os.path.isfile(thing)} {os.path.isdir(thing)}")

