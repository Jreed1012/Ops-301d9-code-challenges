#!/bin/bash

# Prompt user for input directory path
read -p "Enter the directory path: " dir_path

# Check if the provided path is a valid directory
if [ -d "$dir_path" ]; then
    echo "You entered a valid directory path: $dir_path"
else
    echo "Error: The provided path is not a valid directory."
    exit 1
fi