# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 16:09:31 2018

@author: Karthi UK
"""

string = input("Enter some long String: ")
print("Your string is \n {}".format(string))
reverseWord = ""
for word in string.split(" ")[::-1]:
    reverseWord += word
    reverseWord += " "
print("Your Reverse String is: \n {}". format(reverseWord))

    