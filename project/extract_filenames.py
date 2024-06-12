import json

# Load the JSON file
with open('./project/output_files_info.json', 'r') as f:
    data = json.load(f)

# Extract the file names
file_names = [item['file_name'] for item in data]

# Print the file names, each on a new line
for file_name in file_names:
    print(file_name)
