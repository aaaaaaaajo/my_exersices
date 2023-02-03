#!/usr/bin/python3
import math

def f(k):
    f = 1
    x = l
    while x <= k:
        f = f*x
    return f

    
        


n = int(input("enter the first value: "))
m = int(input("enter the second value : "))
l = int(input("enter the initial value of diapason : "))
d = int(input("enter the last value of the diapason : "))
s = 0
c = []
for i in range(0,m+1):
    i = l
    
    i = i + d

a = f(n)
b = f(m)
c = a/(b*f(n-m))


for i in range(0,m+1):
    i = l
    i = i + d
    s = s + c[i]

print("s =" + str(s))
    
    
    
            
       
