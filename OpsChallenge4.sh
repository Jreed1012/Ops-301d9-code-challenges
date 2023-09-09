#!/bin/bash

# Jermain Reed
# Script:    Ops 301 Challenge: Class 04
# Purpose:   
# Task: Hello world (prints “Hello world!” to the screen)
# Ping self (pings this computer’s loopback address)
# IP info (print the network adapter information for this computer)
# Exit
#!/bin/bash

# Function to display the menu
display_menu() {
    clear
    echo "=============================="
    echo "          Main Menu               "
    echo "==============================="
    echo "1. Print 'Hello world!'"
    echo "2. Ping this computer (localhost)"
    echo "3. Display network Adapter information"
    echo "4. Exit"
    echo "================================"
    echo -n "Enter your choice (1/2/3/4): "
}

# Function to print Hello world!
hello_world() {
    clear
    echo "================================="
    echo "         Hello world!               "
    echo "================================="
    echo "Hello world!"
    read -n 1 -s -r -p "Press any key to continue..."
}

# Function to ping the loopback address
ping_self() {
    clear
    echo "================================="
    echo "     Pinging localhost              "
    echo "================================="
    ping -c 4 127.0.0.1
    read -n 1 -s -r -p "Press any key to continue..."
}

# Function to display network adapter information
ip_info() {
    clear
    echo "=================================="
    echo "  Network Adapter Information        "
    echo "=================================="
    ifconfig
    read -n 1 -s -r -p "Press any key to continue..."
}

# Main loop
while true; do
    display_menu
    read choice

    case "$choice" in
        1)
            hello_world 
            ;;
        2)
            ping_self
            ;;
        3)
            ip_info
            ;;
        4)
            echo "Exiting the menu."
            exit 0
            ;;
        *)
            echo "Invalid choice. Please select a valid option (1/2/3/4)."
            ;;
    esac
done