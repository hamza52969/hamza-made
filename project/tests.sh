
#!/bin/bash
echo "Starting tests.sh script execution..."

# Cleanup any pre-existing output files
echo "Cleaning up any pre-existing output files..."
rm -f ./data/dataset1.db
rm -f ./data/dataset2.db

# Verify cleanup
if [ -f ./data/dataset1.db ] || [ -f ./data/dataset2.db ]; then
    echo "Failed to clean up existing output files."
    exit 1
fi
echo "Cleanup successful."

# Running the pipeline
echo "Running the pipeline..."
bash ./project/pipeline.sh

# Check the return value of pipeline.sh
if [ $? -ne 0 ]; then
    echo "Error: pipeline.sh failed."
    exit 1
fi

#run system tests
echo "running system tests:"
python ./project/system_test.py

# Check the return value of system_test.sh
if [ $? -ne 0 ]; then
    echo "Error: system_test.py failed."
    exit 1
fi

