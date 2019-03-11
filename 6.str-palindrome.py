# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 10:36:48 2018

@author: Karthi UK
"""

string = input("Give a random string:\n")
rStr = ""

print("****Method One****")
print("\n")
for char in reversed(string): rStr += char
if string.lower() == rStr.lower():
    print("Your String {} is a Palindrome!".format(string))
else:
    print("Your String {} is a Not Palindrome!".format(string))
    
print("\n")
print("****Method Two****")
if string.lower() == string[::-1].lower():
    print("Your String {} is a Palindrome!".format(string))
else:
    print("Your String {} is a Not Palindrome!".format(string))

