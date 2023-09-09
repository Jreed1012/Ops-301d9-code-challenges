#!/bin/bash

# Jermain Reed
# Script:    Ops 301 Challenge: Class 03
# Purpose:   Chmod777
# Task: Prompts user for input directory path.
#       Prompts user for input permissions number (e.g. 777 to perform a chmod 777)
#       Navigates to the directory input by the user and changes all files inside it to the input setting.
#        Prints to the screen the directory contents and the new permissions settings of everything in the directory.

# Define the Log file path
log_file="script_log.txt"

#Log Messages
log() {
   local message="$1"
   echo "$(date +"%Y-%m-%d %H:%M:%S") $message" >> "log_files"
}
# Prompt user for input permissions number (e.g. 777 to perform a chmod 777)
read -p "Enter the permissions number (e.g. 777): "permissions

# Promtpts user for input directory path.
read -p "Enter the directory path: "dir_path"

# Check if the provided path is a valid directory
if [ -d "$dir_path" ]; then
   echo "You entered a valid directory path: $dir_path"
else 
echo "Error: The provided path is not a valid directory."
 exit 1
fi

# changes all files inside it to the input setting.
chmod -R "permission

# Prints to the screen the directory contents and the new permissions 
# settings of everything in the directory.
echo -e "\nDirectory Contents: "
ls -l

echo -e "\nNew Permission Settings: "
ls -l |awk '{print $1, 9}'