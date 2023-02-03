#!/usr/bin/python3
def fnz(k) :
    return (2*k - 1)
    
n = int(input("enter the value of n: "))

s = 0
k = 1
while True: 
    s = s + fnz(k)
    k = k + 1
    if not k <= n:
        break;

print( str(s) + " it's the final result") 

