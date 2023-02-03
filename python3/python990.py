#!/usr/bin/python3
def translate(phrase):
    translate = ""
    for letter in phrase:
        if letter.lower() in "aouei":
            if letter.isupper():
                translate = translate + "G"
            else:
                translate = translate + "g"
        else:          
            translate = translate + letter
    return translate
    
print(translate(input("enter ur psrase: ")))