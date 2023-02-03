#!/usr/bin/python3
translate = open("python990.py", "r")
for string in translate.readlines():
    print(string)
#print(translate.readlines()[2])
 
translate.close()