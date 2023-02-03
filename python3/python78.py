#!/usr/bin/python3
print("Content-type:text/html\n")
import os    #библиотека для доступа к функциям ос
import sys  # тоже самое
import re #библиотека регулярных выражений
import json 
import cgi
import cgitb
cgitb.enable()

#sys.exit()
from datetime import datetime





def flog_out(fs_str):
    # Getting the current date and time
    dt = datetime.now()
    # getting the timestamp
#    ts = datetime.timestamp(dt)
    file = open("/var/log/barbara-cgi/python78.log", "a")
    file.write("[INFO] "+ str(dt) + " " + fs_str  + "\n")
    file.close()
flog_out("start program")
flog_out("try open config file")
try: 
    with open('/opt/test/personal.json', "r", encoding="utf-8") as f_file_json: #utf-8 кодировка на кирилицу 
     o_text = json.load(f_file_json) #  венгерская запись. через подчеркивания мы указываем сущность переменных (о это сложный объект)
     
#     jsonData = data[personal]
#        for x in jsonData:
#            keys = x.keys()
except:
    print("<H1>invalid json</H1> ")
    flog_out("can't parse config json ")
    sys.exit()
flog_out("we are parsing input parametrs")
form = cgi.FieldStorage() #список ключей вызова
l_personal = o_text["personal"]

l_arg_keys = form.keys()
#print (str(l_arg_keys))
#sys.exit()
if l_arg_keys[0] == "info" :
    flog_out("found parameter info")
    l_json_0 = l_personal[0]
    for key in l_json_0.keys():
        print (str(key)) 
    #распечатать список кл 
else: 
    flog_out("executing query")
    lfound = False     
    #/cgi-bin/python78.py?hobby=malen
    for s_field in form.keys():  #ключи парамеров. в цикле ключи по очереди попадают в индекс цикла - переменную s_field 
        s_pattern = form.getvalue(s_field)   #вычитываем очередное значение параметра вызова по ключу имя которого в переменной s_field 
     
    #s_field = input("enter type of information in which u interested: ") #вторая переменная нужна для конкретизации поиска
    #s_pattern = input("enter information in which u interested: ") #строковая s
        s_pattern1 = ".*" + s_pattern + ".*"  # в s_pattern1 мы передаем значение s_pattern с регулярным выражением. .* означает искать по всему файлу. то есть 
    #мы даем значение команы которая ищет заданную информацию по всему файлу
        lfound = False  # мы добавляем еще один флаг. в случае если мы ничего не найдем то получим только одну фразу что сравнения отсутсвуют
        for index in l_personal:  #цикл для переменных внути массива. о_текст это переменная в которую мы поместили вывод прочитанного текста
    #        print("compare : " + s_pattern1 + " " + index[s_field])
            match = re.search( s_pattern1, index[s_field] )  #ищем информацию. индекс это пременные внутри массива ,[s_field] а это тип данных
        


            if match:
                lfound = True  
                print("found " + index ["name"] + " - " + match.group() +"<br>")  #если оно находит данные то оно выдает имя персоны и тип запрашиваемых данных
    if not lfound:
        print("сравнений не обнаружено")
        
flog_out("end of program")


