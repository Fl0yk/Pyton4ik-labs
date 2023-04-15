import re
from Task2.Constans import ERROR_INPUT, YES, NO

def username_check(username : str):                     
    while(re.findall(r"[?!#$\"/\\\s]+", username)       #Т.к. контейнер пользователя - отдельный файл,
            or username.isspace() or username == ""):   #в названии которого есть имя, то на всякий случай
        print(ERROR_INPUT)                              #при обращении к файлу, имя должно быть нормальным
        username = input()
    return username

def yes_no(y_n : str):
    while(True):
        if(y_n == YES):
            return True
        elif (y_n == NO):
            return False
        print(ERROR_INPUT)
        y_n = input()