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



name = '' + list[r(0, len(list)-1)] + " " + list[r(0, len(list)-1)]

print(name)