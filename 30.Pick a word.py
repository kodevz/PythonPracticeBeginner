# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 10:47:24 2018

@author: Karthi UK
"""

import random

words = []

def sowpods():
    with open('sowpods/sowpods.txt','r') as openFile:
        line = openFile.readline().strip()
        words.append(line)
        while line:
          line = openFile.readline().strip()
          words.append(line)     
    rIdx = random.randint(0,len(words));
    print(words[rIdx])

if __name__ == "__main__":
    sowpods()

    
    
    