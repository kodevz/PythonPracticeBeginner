# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 13:45:57 2018

@author: 18096
"""

import random

def cpuNumber():
    return random.randint(10,100)
    
def doGame(cpu):
    userIn = int(input("Guess Your Number: "))
    if cpu == userIn:
        print("Your Guess Is Correct. You Won this Match")
        usrCmd = input("Want Continue? Say [Y/N]: ")
        if usrCmd in ('Y','y'): 
            doGame(cpuNumber()) 
        else:False
    if cpu > userIn:
        print("Try To Guess Greaterthan Number")
        doGame(cpu)
    if cpu < userIn:
        print("Try to Guess Less Than Number")
        doGame(cpu)
        
if __name__ == "__main__":
    
    cpuIns = cpuNumber()
    while True:
        if not doGame(cpuIns):break