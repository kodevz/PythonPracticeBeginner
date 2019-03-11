# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 09:26:18 2018

@author: 18096
"""

inpt = int(input("Enter One Number:\n"))
nType = "Odd"
if inpt % 2 == 0:
    nType = "Even"
    
print("Your Number is {}".format(nType))

num1 = int(input("Enter Any number your wish : "))
num2 = int(input("Enter any number for devide: "))

if num1 % num2 == 0:
    nType = "Even"
    print("Your Number {} is divisible by {}". format(num1, num2))
else:
    print("Your Number {} is Not divisible by {}". format(num1, num2))
