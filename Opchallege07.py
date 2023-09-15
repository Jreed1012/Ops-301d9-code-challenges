#!/usr/bin/env python3
# Script:                       Op Challenge 7
# Author:                       Jermain 
# Date of latest revision:      09/15/2023
# Purpose:       Script must ask the user for a file path and read a user input string into a variable.
# Script must use the os.walk() function from the os library.
# Script must enclose the os.walk() function within a python function that hands it the user input file path.

import os

def list_files_and_directories(user_path):
    try:
        for root, dirs, files in os.walk(user_path):
            print(f"Directory: {root}")
            for file in files:
                print(f"  File: {file}")
            for directory in dirs:
                print(f"  Sub-directory: {directory}")
    except FileNotFoundError:
        print(f"Directory doesn't exist: {user_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    user_path = input("Enter a directory: ")
    list_files_and_directories(user_path)