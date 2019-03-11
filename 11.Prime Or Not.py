# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 15:06:52 2018

@author: Karthi Uk
"""


def userInput():
    return input("Enter Your Number: ")

num = int(userInput())
print(num)

if num % 2 == 0:
    print("Your Given Number {} is NotPrime". format(num))    
else:
    print("Your Given Number {} is Prime". format(num))    
    

