#!/usr/bin/python3
import math

n = int(input("enter the value of n: "))
a = []
for i in range(n):
    a.append(0.0)
a[0]=1
a[1]=1
s = 2

i = 3
while i < n:
      a[i] = a[i-1] + a[i-2]
      s = s + a[i]
      i = i + 1
      
print(str(s))