# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 10:58:37 2018

@author: Karthi UK
"""

nx = []
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

print("********Method One********")
for e in a:
    if len(nx) < 7: nx.append(e)
    

print("********Method Two For single line********")
print(filter(lambda nx: len(nx) < 4, a))
print(nx)





