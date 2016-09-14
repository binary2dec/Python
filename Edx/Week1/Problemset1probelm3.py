# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 13:55:53 2016

@author: Binary2Dec
"""
"""
iterates through the string to find the longest
sequential character set
requires a variable known as "s"
for example: s = 'lksjdfgjsdlfkhjnmn'
"""

b = ""
y  = ""
z = ""

for x in range(len(s)):
    if len(b) > len(z):
        z = b
    if s[x] >= s[x-1]:
        b += s[x]
    elif s[x] <= s[x-1]:
        y = b
        b = ""
        b += s[x]
if len(b) > len(z):
        z = b
print("Longest substring in alphabetical order is: " + z)
