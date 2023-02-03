#!/usr/bin/python3
import math

k = int(input("enter the k's value: "))
f = 1
i = 1

while i <= k:
    f = f*i
    i = i + 1
 
print(" f =" + str(f))