#!/usr/bin/env python3
import os
from random import randint as r
list = []


directory_in_str = os.path.dirname(__file__) + "/lists"

directory = os.fsencode(directory_in_str)

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename.endswith(".txt"):
        with open(directory_in_str+ '/' + filename) as f:
            for line in f.readlines():
                list.append(line)
    else:
        continue    

amount = str(input())
if amount.isdigit():
    amount = int(amount)
    if (amount < 2):
        print("[-] Input can't be less than 2")
    elif (amount > len(list)):
        print("[-] Input can't be greater than the length of the list of words")
        print("List lenght: " + str(len(list)))
    else:
        name = ''
        for x in range(0, amount):
            name = name + '' + list[r(0, len(list)-1)] + " " 
        print(name)

else:
    print("Input is not a digit")

