# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 15:38:44 2018

@author: Karthi UK
"""

def userInput():
    return input("How many fibanocci numbers do you want?: ")

def fibo():
    a = 0
    b = 1
    iterate = 0
    fibList = [a,b]
    upto = int(userInput())
    while iterate < upto:
        fibList.append(a + b)
        a = b
        b = a + b
        iterate += 1
        
    print(fibList)

fibo()
    
    
    
    