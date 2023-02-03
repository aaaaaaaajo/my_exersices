a = int(input("enter the first value: "))
b = int(input("enter the second value: "))
r = 2
a = a**r
b = b**r

if a != 0 and b !=0:
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
elif a !=0 and b == 0:
    print("impossible to count")
elif a == 0 and b !=0:
    print("impossible to count")
else:
    print("impossible to count")
