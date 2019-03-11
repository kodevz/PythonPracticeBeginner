# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 15:57:22 2018

@author: Karthi UK
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

"""
    This is First Concept
"""
c = list(set(a) & set(b))
n = []

for e in b: n.append(e)
for e in a: 
    if e in b and not e in n: n.append(e)
print(n)