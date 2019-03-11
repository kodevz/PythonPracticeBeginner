# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 10:55:49 2018

@author: Karthi UK
"""

import random

def chooseRandomWord():
    with open('sowpods/sowpods.txt','r') as openFile:
        line = openFile.readline().strip()
        words.append(line)
        while line:
          line = openFile.readline().strip()
          words.append(line)     
    rIdx = random.randint(0,len(words));
    return words[rIdx]
    

def showAns():
    for dash in range(0,len(string)):
        if len(userAns) > dash: print(userAns[dash ].upper(), end = " ")
        else:print("_", end = " ")
    
    

def guessLetter():
    global userAns
    global wrongAtmpt
    print('\n You Have {} attempt Left'.format(6 - wrongAtmpt))
    
    if wrongAtmpt == 6:
        print("Sorry You Lose This Game..")
        return False
    
    userGuess = input("Guest Your Letter : ")
    
    print(userGuess)

    if string[len(userAns)].lower() == userGuess.lower():
        userAns += userGuess.lower()
        
        print("Your Guess is Correct!!! \n")
        
        if string.lower() == userAns.lower():
            print("You Won This Game. You Found Correct!!!! \n")
            return False
    
        if len(userAns) > 0:
            showAns()
            guessLetter()
    else:
        wrongAtmpt += 1;
        showAns()
        guessLetter()
    


if __name__ == "__main__":
    print("Welcome to Hangman!")
    userAns = ''
    string = chooseRandomWord()
    wrongAtmpt = 0
    words = []
    showAns()
    
    print(string)
    
    while True:
        if guessLetter():pass
        else:
            usr_cmd = input("Would you like to continue this game? Press[Y/n] :")
            if usr_cmd.lower() == 'y':
                userAns = ''
                string = chooseRandomWord()
                print(string)
                wrongAtmpt = 0
                words = []
                showAns()
            else:break
               
    
    