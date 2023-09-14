#!/bin/bash

# Jermain Reed
# Script:    Ops 301 Challenge: Class 05
# Purpose:  Include execution of the following bash commands inside your Python script:

import os

# Execute 'whoami' command
whoami_result = os.popen('whoami').read()
print("Output of 'whoami' command:")
print(whoami_result)

# Execute 'ip a' command
ip_a_result = os.popen('ip a').read()
print("\nOutput of 'ip a' command:")
print(ip_a_result)

# Execute 'lshw -short' command
lshw_short_result = os.popen('lshw -short').read()
print("\nOutput of 'lshw -short' command:")
print(lshw_short_result)







