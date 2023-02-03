#!/usr/bin/python3
a = int(input("enter less number: "))
c = int(input("enter bigest number: "))
if c > a: 
    b = a
    e = c
else: 
    b = c
    e = a
catch = "false"
while catch == "false":
    x = b+int((e - b)/2)
 
    ur_number = input("is ur number is : " + str(x) + " (y/n)") 
    if ur_number == "y":
        print("i win")
        catch = "true"
        continue
      
    m = input("is ur number > " + str(x) + " (y/n)")
    if m == "y":
       b = x
    else:
       e = x
#eof
