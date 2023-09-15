#!/bin/bash

directory_path="/home/family-guy/Documents/python/python-programs/restart/basics/find type of"

# Check if the directory exists
if [ ! -d "$directory_path" ]; then
    echo "Directory does not exist: $directory_path"
    exit 1
fi

# Get the latest modified .cpp file
latest_file=$(find "$directory_path" -name "*.py" -type f -print0 | xargs -0 ls -lt | head -n 1 | awk '{print $NF}')

# Check if a .cpp file was found
if [ -z "$latest_file" ]; then
    echo "No .py files found in the directory."
    exit 1
fi

echo "Latest modified .py file: $latest_file"

filename=$(basename "$latest_file")
python3 $filename
