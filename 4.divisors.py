# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 10:01:23 2018

@author: Karthi UK
"""


x = []
num = int(input("Give any number:\n"))
for e in range(2, num + 1):
    if num % e == 0:
        x.append(e)
print(x)
