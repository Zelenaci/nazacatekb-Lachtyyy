# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 20:00:10 2017

@author: Lachtyyy
"""

a = input ("Obraz - Kolik řádků obrázku se má vytisknout? ")
a = int (a)
x = 0
x = a / 18

while x >= 1:
    print ("****\n***\n**\n*\n \n    *\n   ***\n  *****\n *******\n*********\n \n*\n**\n***\n****\n***\n**\n*")
    x = x - 1
y = a % 18
if y >= 1:
    print("****")
if y >= 2:
    print ("***")
if y >= 3:
    print ("**")
if y >= 4:
    print ("*")
if y >= 5:
    print (" ")
if y >= 6:
    print ("    *")
if y >= 7:
    print ("   ***")
if y >= 8:
    print ("  *****")
if y >= 9:
    print (" *******")
if y >= 10:
    print ("*********")
if y >= 11:
    print (" ")
if y >= 12:
    print ("*")
if y >= 13:
    print ("**")
if y >= 14:
    print ("***")
if y >= 15:
    print ("****")
if y >= 16:
    print ("***")
if y >= 17:
    print ("**")