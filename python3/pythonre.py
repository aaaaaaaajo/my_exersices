#!/usr/bin/python3
def raise_to_power(base, num):
    result = 1
    for index in range(num):
        result = result * base
    return result
    
print(raise_to_power(4, 3))
