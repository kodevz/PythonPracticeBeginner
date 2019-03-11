# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 12:24:14 2018

@author: 18096
"""

dashes = ' --- '
pipes = '|   '

def drawSquare():
    print(dashes)
    print(pipes) 

if __name__ == "__main__":
    size = int(input('What size game board would you like? \n'))

    for x in range(0, size-1):
        dashes = dashes + '--- '
        pipes = pipes + '|   '

    pipes = pipes + '|'

    for y in range(0,size):
        drawSquare()

    print(dashes)
      
        
            
            
   
   

