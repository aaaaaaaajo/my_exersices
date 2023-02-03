#!/usr/bin/python3
#it worked

class Slave:
    def __init__ (self, f_name, f_age):
        self.__name = f_name
        self.__age = f_age

    def information(self):
        print(self.__name, self.__age)

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

class Gym:
    def __init__(self):
        self.__count = 0
        self.__spusok = [] # ("n1" 123), ("n2" 432)

    def add_slave(self, f_slave):
        self.__spusok.append(f_slave)

    def every_slave(self):
        for l_slave in self.__spusok:
            l_slave.information()

    def younger_slave(self):
        for l_i in self.__spusok:
            l_i.get_age()

l_gym = Gym()
count=int(input("input count:")) # 3
for i in range(count):
    l_name=str(input("name:"))
    l_age=int(input("age:"))
    l_slave = Slave(l_name, l_age)
    l_gym.add_slave(l_slave)

l_gym.every_slave()