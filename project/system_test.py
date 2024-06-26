import json
import os
import sys

# Read expected files from the JSON file
with open('./project/output_files_info.json', 'r') as f:
    output_files_info = json.load(f)
    expected_files = [item['file_name'] for item in output_files_info]

# Define the data directory
data_dir = './data/'

# Function to check if file exists in any sub-folder
def file_exists_in_subfolders(file_name, directory):
    for root, dirs, files in os.walk(directory):
        if file_name in files:
            return True
    return False

# Check if all expected files exist
all_files_exist = True
for db_file in expected_files:
    if file_exists_in_subfolders(db_file, data_dir):
        print(f"Expected file '{db_file}' found.")
    else:
        print(f"Expected file '{db_file}' not found in sub-folders of {data_dir}")
        all_files_exist = False

# Output the result of the test
if all_files_exist:
    print("All expected files exist. System test passed!")
    sys.exit(0)  
else:
    print("Not all expected files found in sub-folders of {data_dir}. System test failed!")
    sys.exit(1) 
