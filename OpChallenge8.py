#!/usr/bin/env python3
# Script:                       Op Challenge 08
# Author:                       Jermain 
# Date of latest revision:      09/08/2023
# Objective: Assign to a variable a list of ten string elements.
# Print the fourth element of the list.
# Print the sixth through tenth element of the list.
# Change the value of the seventh element to “onion”.

my_list = ["Carrot", "Scallion", "Leek", "Pepper", "Bean", "Fennel", "Wild Cabbage", "Broccoli", "Rutabaga", "Pumpkin"]
print("Fourth element:", my_list[3])
print("Sixth through tenth elements:", my_list[5:10])
my_list[6] = "onion"
print("Updated list:", my_list)