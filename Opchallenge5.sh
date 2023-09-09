#!/bin/bash


# Jermain Reed
# Script:    Ops 301 Challenge: Class 05
# Purpose:   Print to the screen the file size of the log files before compression
#Compress the contents of the log files listed below to a backup directory
#/var/log/syslog
#/var/log/wtmp
#The file name should contain a time stamp with the following format -YYYYMMDDHHMMSS

# Define the backup directory
backup_dir="/var/log/backups"

# Create the backup directory if it doesn't exist
mkdir -p "$backup_dir"

# Timestamp
timestamp=$(date +"%Y%m%d%H%M%S")

# Define an associative array of log files to compress
declare -A log_files=(
    ["/var/log/syslog"]="Syslog"
    ["/var/log/wtmp"]="Wtmp"
)

# Function to compress and backup a log file
compress_and_backup() {
    local source_file="$1"
    local base_name=$(basename "$source_file")
    local compressed_file="$backup_dir/$base_name-$timestamp.zip"
    
    if [ ! -e "$source_file" ]; then
        echo "Error: '$source_file' does not exist."
        return
    fi
    
    gzip -c "$source_file" > "$compressed_file"
    echo "Compressed '${log_files[$source_file]}' to '$compressed_file'"
    echo "File size of '$compressed_file': $(du -sh "$compressed_file" | awk '{print $1}')"
    > "$source_file" # Clear the contents of the original log file
}

# Compress and backup log files
for source_file in "${!log_files[@]}"; do
    compress_and_backup "$source_file"
done
Each of these versions achieves the same tasks but with different coding styles and approaches. Choose the one that suits your preference or coding style best.





