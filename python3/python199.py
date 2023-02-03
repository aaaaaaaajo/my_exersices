#!/usr/bin/python3
import math 

def f(k):
    f = 1
    i = 1
    while i <= k:
        f = f*i
        i = i + 1
    return(f)

n = int(input("enter the first value of factorial's formula: "))
m = int(input("enter the second value of factorial's formula: "))   

a = f(n)
b = f(m)
c = a /(b*f(n-m))

print("c =" + str(c))


