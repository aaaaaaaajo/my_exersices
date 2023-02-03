#!/usr/bin/python3
import math
def fnz(k):
    return(2*k - 1)
    
n = float(input("enter the number of numbers: "))
k = float(input("enter the k's value: "))
d = float(input("enter the adding of number d: "))
r = float(input("enter in which rase of power u wanna do with numbers: "))
s = 0

#for i=k to n step d. it means that i's value gain diapason between k to n and added to d 
i = k
while i < n : #i less than n cause it must be diapason between k to n, so i can't be bigger than n
      
      s = s + (fnz(i))**r
      i = i + d
print( "s =" + str(s))
