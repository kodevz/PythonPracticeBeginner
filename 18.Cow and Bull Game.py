# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 08:20:55 2018

@author: Karthi UK
"""

import random

def cupNumber():
    return random.randint(1000,2000)

def checkUserInput(userInput):
    digits = len(str(abs(userInput)))
    if digits != 4:
        print("Your Have Entered {} digits Number. Please Enter 4 Digit Number".format(digits))
        return False
    else:
        return True
    
def findBullAndCow():
    score = 0
    cpuInput = cupNumber()
    print(cpuInput)
    userInput = int(input("Guess Your Number : "))
    
    if cpuInput == userInput:
        print("Game Over !!!!")
        return  False
      
    if checkUserInput(userInput):
        cpuInsList = [int(x) for x in str(cpuInput)]
        userInsList = [int(x) for x in str(userInput)]
        
        ##Method One for Iteration
        #Find Cows
        #for u in userInsList:
            #idx = userInsList.index(u)
            #if u == cpuInsList[idx]:
                #cows.append(u)
        
        #Find Bulls
        #for u in userInsList:
            #idx = userInsList.index(u)
            #if u in cpuInsList and u != cpuInsList[idx]:
                #bulls.append(u)
        
        ##Method Two for List Comprehensive
        #Find Cows
        cows = [c for c in userInsList if c == cpuInsList[userInsList.index(c)]]
        #Find Bulls
        bulls = [b for b in userInsList if b in cpuInsList and b != cpuInsList[userInsList.index(b)]]
        
        score += 1
        print("{} cows, {} bulls".format(len(cows),len(bulls)))
        print("Your Score is {}".format(score))
        
    userCmd = input("Do you want to continue this game? Press [Y/N] : ")    
    if userCmd in ("y","Y"):return  True
    else: return False
        
if __name__ == "__main__":
    while True:
        if findBullAndCow():pass
        else: break
            
    