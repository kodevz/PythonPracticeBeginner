# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 12:23:44 2018

@author: Karthi UK
"""

import random
score = 0
while True:
    cpu = random.randint(2,10)
    ansstatus = True
    print(cpu)
    print("CPU Played...")
    print("CPU Number is *, You Guess this number")
    attempt = 3;
    while ansstatus:
        if attempt > 0:
            attempt -= 1
            userInput = int(input("Enter Your Guess: "))
            if cpu == userInput:
                score += 1
                print("You Guess Correct");
                print("Your are Score is  {}".format(score))
                ansstatus = False
        else:
            print("You Lose Your Game");
            ansstatus = False
    
    uquit = input("do you want to continue ? [y/n]")
    if uquit == 'y': continue
    else:break

    
    
    

    