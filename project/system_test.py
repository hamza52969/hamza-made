import json
import os
import sys

# Read expected CSV files from the JSON file
with open('./project/output_files_info.json', 'r') as f:
    output_files_info = json.load(f)
    expected_csv_files = [item['file_name'] for item in output_files_info]

# Define the data directory
data_dir = 'D:/FAU_degree/sem_5/MADE/project/hamza-made/data'

# Function to check if file exists in any sub-folder
def file_exists_in_subfolders(file_name, directory):
    for root, dirs, files in os.walk(directory):
        if file_name in files:
            return True
    return False

# Check if all expected files exist
all_files_exist = True
for csv_file in expected_csv_files:
    if file_exists_in_subfolders(csv_file, data_dir):
        print(f"Expected file '{csv_file}' found.")
    else:
        print(f"Expected file '{csv_file}' not found in sub-folders of {data_dir}")
        all_files_exist = False

# Output the result of the test
if all_files_exist:
    print("All expected files exist. System test passed!")
    sys.exit(0)  # Exit with success code
else:
    print("Not all expected files found in sub-folders of {data_dir}. System test failed!")
    sys.exit(1)  # Exit with failure code
