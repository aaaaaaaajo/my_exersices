#!/usr/bin/python3
import json 

import re #библиотека регулярных выражений
try: 
    with open('/opt/test/personal.json', "r", encoding="utf-8") as f_file_json: #utf-8 кодировка на кирилицу 
     o_text = json.load(f_file_json) #  венгерская запись. через подчеркивания мы указываем сущность переменных (о это сложный объект)
except:
    print("invalid json ")
s_field = input("enter type of information in which u interested: ") #вторая переменная нужна для конкретизации поиска
s_pattern = input("enter information in which u interested: ") #строковая s
s_pattern1 = ".*" + s_pattern + ".*"  # в s_pattern1 мы передаем значение s_pattern с регулярным выражением. .* означает искать по всему файлу. то есть 
#мы даем значение команы которая ищет заданную информацию по всему файлу
lfound = False  # мы добавляем еще один флаг. в случае если мы ничего не найдем то получим только одну фразу что сравнения отсутсвуют
for index in o_text["personal"]:  #цикл для переменных внути массива. о_текст это переменная в которую мы поместили вывод прочитанного текста
#    print("compare : " + s_pattern1 + " " + index[s_field])
    match = re.search( s_pattern1, index[s_field] )  #ищем информацию. индекс это пременные внутри массива ,[s_field] а это тип данных
    


    if match:
        lfound = True  
        print("found " + index ["name"] + " - " + match.group()) #если оно находит данные то оно выдает имя персоны и тип запрашиваемых данных
if not lfound:
    print("сравнений не обнаружено")
    


