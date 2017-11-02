# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 20:00:10 2017

@author: Lachtyyy
"""

a = input ("Kolik řádků obrázku se má vytisknout? ")
a = int (a)
x = 0
x = a / 18

while x >= 1:
    print ("****\n***\n**\n*\n \n    *\n   ***\n  *****\n *******\n*********\n \n*\n**\n***\n****\n***\n**\n*")
    x = x - 1
i = a % 18
if i >= 1:
    print("****")
if i >= 2:
    print ("***")
if i >= 3:
    print ("**")
if i >= 4:
    print ("*")
if i >= 5:
    print (" ")
if i >= 6:
    print ("    *")
if i >= 7:
    print ("   ***")
if i >= 8:
    print ("  *****")
if i >= 9:
    print (" *******")
if i >= 10:
    print ("*********")
if i >= 11:
    print (" ")
if i >= 12:
    print ("*")
if i >= 13:
    print ("**")
if i >= 14:
    print ("***")
if i >= 15:
    print ("****")
if i >= 16:
    print ("***")
if i >= 17:
    print ("**")