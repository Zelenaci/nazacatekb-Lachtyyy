# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 20:00:10 2017

@author: Lachtyyy
"""

l = int(input("Kolik prvků Fibonacciho posloupnosti se má vypsat? >>> "))
x = 0
y = 1
i = 0
for i in range(l):
    i = x + y
    y = x
    x = i
    print(i)