# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 12:07:53 2018

@author: Karthi UK
"""
names = {}
with open('sample.txt','r') as open_file:
    lines = open_file.readlines()
    for line in lines:
        line = str(line).rstrip()
        if line in names.keys():
            names.update({line : names.get(line) + 1})
        else:
            names.update({line:1})
    print(names)
open_file.close()
        