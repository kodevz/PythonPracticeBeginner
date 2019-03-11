# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 16:21:20 2018

@author: Karthi Uk
"""
import string
import random

def passwordGenerator(pplength):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    special = string.punctuation
    number = string.digits
    everything = upper + lower + special + number
    password = random.sample(everything, 8)
    for p in password:
        password =  "".join(password)
    return password
length = int(input("Enter Your password length :\n"))
print(passwordGenerator(length))