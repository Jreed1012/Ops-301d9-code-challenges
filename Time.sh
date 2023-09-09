#!/bin/bash

# Jermain Reed
# Script:    Ops 301 Challenge
# Purpose:   Append date and time to a file
# Why:       Copies /var/log/syslog to the current working directory
#            appends the current date and time to the filename

# Copy syslog to a timestamped file
cp /var/log/syslog "syslog_$(date +"%Y-%m-%d_%H-%M-%S").log"

# Check if the copy operation was successful
if [ $? -eq 0 ]; then
    echo "Log file copied successfully."
else
    echo "Error: copy not complete."
fi

# Create a file and add some lines to it
echo "original file before append: "
cat testfile.txt

# Append a new string with the current date and time
echo "My new string with date: $(date)" >> testfile.txt

echo "appended file: "
cat testfile.txt

# End
