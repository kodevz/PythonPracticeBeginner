# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 09:41:36 2018

@author: Karrthi
"""

nx = []
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

for e in a:
    if e < 5:
        nx.append(e)

print("1)\n")
print(nx)


print("\n2)\n")
print(list(filter(lambda nx: (nx < 5), a)))

num = int(input("Enter Your Number : "))

nx = []
for e in a:
    if e < num:
        nx.append(e)

print("\n3)\n")
print(nx)



