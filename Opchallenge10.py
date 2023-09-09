#!/usr/bin/env python3
# Script:                       Op Challenge 10
# Author:                       Jermain 
# Date of latest revision:      09/09/2023
# Purpose:                      File Handling
# Objective: Using file handling commands,
# create a Python script that creates a new .txt file, appends three lines, prints to the screen the first line, then deletes the .txt file.



# Create a new .txt file and append three lines
with open("Example.txt", "w") as file:
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")
    file.write("This is the third line.\n")

# Open the file and print the first line
try:
    with open("Example.txt", "r") as file:
        first_line = file.readline()
        print("First Line:", first_line.strip())  
except FileNotFoundError:
    print("File 'Example.txt' Sorry this file doesn't exist.")

# Delete the file
import os
try:
    os.remove("Example.txt")
    print("File 'Example.txt' deleted.")
except FileNotFoundError:
    print("File 'Example.txt' Sorry this file doesn't exist.")