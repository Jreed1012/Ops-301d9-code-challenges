#!/usr/bin/env python3
# Script:                       Op Challenge 11
# Author:                       Jermain 
# Date of latest revision:      09/11/2023
# Purpose:                      File Handling
# Objective:Time spent by normal processes executing in user mode
#Time spent by processes executing in kernel mode
#Time when system was idle
#Time spent by priority processes executing in user mode
#Time spent waiting for I/O to complete.
#Time spent for servicing hardware interrupts
#Time spent for servicing software interrupts
#Time spent by other operating systems running in a virtualized environment
#Time spent running a virtual CPU for guest operating systems under the control of the Linux kernel 


import psutil

def get_system_info():
         # Time spent by other operating systems running in a virtualized environment
    guest_time = psutil.cpu_times().guest
    
    # Time spent for servicing hardware interrupts
    irq_time = psutil.cpu_times().irq
    
    # Time spent by processes executing in kernel mode
    system_time = psutil.cpu_times().system
    
    # Time spent by normal processes executing in user mode
    user_time = psutil.cpu_times().user
    
    # Time spent for servicing software interrupts
    softirq_time = psutil.cpu_times().softirq
    
    # Time spent waiting for I/O to complete
    io_wait_time = psutil.cpu_times().iowait
    
    # Time spent when system was idle
    idle_time = psutil.cpu_times().idle
    
    # Time spent by priority processes executing in user mode
    priority_user_time = psutil.cpu_times().nice
    
    # Time spent running a virtual CPU for guest operating systems
    guest_nice_time = psutil.cpu_times().guest_nice
    
    # Print the results with the mixed order
    print(f"Time spent by other operating systems running in a virtualized environment: {guest_time} seconds")
    print(f"Time spent for servicing hardware interrupts: {irq_time} seconds")
    print(f"Time spent by processes executing in kernel mode: {system_time} seconds")
    print(f"Time spent by normal processes executing in user mode: {user_time} seconds")
    print(f"Time spent for servicing software interrupts: {softirq_time} seconds")
    print(f"Time spent waiting for I/O to complete: {io_wait_time} seconds")
    print(f"Time when system was idle: {idle_time} seconds")
    print(f"Time spent by priority processes executing in user mode: {priority_user_time} seconds")
    print(f"Time spent running a virtual CPU for guest operating systems: {guest_nice_time} seconds")



if __name__ == "__main__":
    get_system_info()