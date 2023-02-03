#!/usr/bin/python3
import math
def fnz(k):
    return(2*k - 1)
    
n = int(input("enter the number of numbers: "))
k = int(input("enter the k's value: "))
d = int(input("enter the adding of number d: "))
r = int(input("enter in which rase of power u wanna do with numbers: "))
s = 0

while True:
    s = s + (fnz(k))**r
    k = k + d
    if not k <= n:
        break;
        
print(str(s) + "it's a final result")
