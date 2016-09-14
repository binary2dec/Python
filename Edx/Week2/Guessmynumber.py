# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 10:13:39 2016

@author: Binary2Dec
"""

x = ""
h = 100
l = 0

print("Please think of a number between 0 and 100!")


while x != 'c':
    
    answer = (l + h)//2
    
    print("Is your secret number " + str(answer) + "?")
    
    x = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")

    if x == 'l':
        l = answer
        
    elif x == 'h':
        h = answer
    
    elif x == 'c':
        break
    
    else:
        print("Sorry, I did not understand your input.")
        
        
        
print("Game over.  Your secret number was: " + str(answer))
        
        
        