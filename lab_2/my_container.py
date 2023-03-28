import re
from constans import PATH, NOT_ELEM, ERROR_ADD

class Container:
    
    def __init__(self, *args):
        self.__container = set()
        try:                            #Т.к. некоторые типы даных не хешируемые, то добавление оберрнул в трай кетч
            self.__container.update(set(args))
        except Exception:
            print(ERROR_ADD)
        
    def __str__(self):
        return self.__container.__str__()
    
    
    def find(self, *args):
        elements = self.__container.intersection(args)
        if elements:
            return elements
        
        return NOT_ELEM
    
    def add(self, *args):
        try:
            self.__container.update(set(args))
        except Exception:
            print(ERROR_ADD)
        
    def _add_set(self, my_set : set):
        self.__container.update(my_set)
        
    def remove(self, element):
        if (element not in self.__container):
            return
        
        self.__container.remove(element)
        
    def grep(self, regex : str):
        result = list()
        
        for elem in self.__container:
            if (re.fullmatch(regex, elem.__str__())):
                result.append(elem.__str__())
        
        if result:
            return result
        
        return NOT_ELEM
    
    def list(self):
        for elem in self.__container:
            print(elem)
    
    def save(self, path : str):
        with open(path, 'w') as file:
            file.writelines((elem.__str__() + "\n") for elem in self.__container)
            
    def load(self, path : str):
        try:
            file = open(path)       #Точно ли нормально работает? По поводу открытия файла без закрытия
        except IOError:
            print("file does not exist")
        else:
            with open(path, 'r') as file:
                load_elem = set(elem.rstrip() for elem in file.readlines())
            #print(load_elem)
            self._add_set(load_elem)
        
        
class UsersAndContainers:
    
    def __init__(self):
        self.__users = dict()
        with open(PATH + "Containers/" + "users.txt", 'r') as file:
            for user_cont in file.readlines():
                tmp = user_cont.split()
                #Чтоб отделить путь от пользователя, убираем спец символы в конце строки и срезаем помле имени и пробела
                self.__users[tmp[0]] = user_cont.rstrip()[len(tmp[0]) + 1::]
                
    def __del__(self):
        with open(PATH  + "Containers/" + "users.txt", 'w') as file:
            for user in self.__users:
                file.write(user + " " + self.__users[user] + "\n")
                
    def add_user(self, username : str):
        self.__users[username] = PATH + "Containers/" + username + "Container.txt"
        
    def find_user(self, username : str):
        return self.__users[username]
    
    def list_users(self):
        print(self.__users)