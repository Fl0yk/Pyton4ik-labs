import re
from constans import PATH

class Container:
    
    def __init__(self, *args):
        self.__container = set(args)
        
    def __str__(self):
        return self.__container.__str__()
    
    
    def find(self, *args):
        elements = self.__container.intersection(args)
        if elements:
            return elements
        
        return "No such elements"
    
    def add(self, *args):
        self.__container.update(set(args))
        
    def _add_set(self, my_set : set):
        self.__container.update(my_set)
        
    def remove(self, element):
        self.__container.remove(element)
        
    def grep(self, regex : str):
        result = list()
        
        for elem in self.__container:
            if (re.fullmatch(regex, elem.__str__())):
                result.append(elem.__str__())
        
        if result:
            return result
        
        return "No such elements"
    
    def list(self):
        for elem in self.__container:
            print(elem)
    
    def save(self, path : str):
        with open(path, 'w') as file:
            file.writelines((elem.__str__() + "\n") for elem in self.__container)
            
    def load(self, path : str):
        try:
            file = open(path)
        except IOError:
            print("file does not exist")
        else:
            with open(path, 'r') as file:
                load_elem = set(elem.rstrip() for elem in file.readlines())
            print(load_elem)
            self._add_set(load_elem)
        
        
class UsersAndContainers:
    
    def __init__(self):
        self.__users = dict()
        with open("users.txt", 'r') as file:
            for user_cont in file.readlines():
                user_cont = user_cont.split()
                self.__users[user_cont[0]] = user_cont[1]
                
    def __del__(self):
        with open("users.txt", 'w') as file:
            for user in self.__users:
                file.write(user + " " + self.__users[user] + "\n")
                
    def add_user(self, username : str):
        self.__users[username] = PATH + username + "Container.txt"
        
    def find_user(self, username : str):
        return self.__users[username]
    
    def list_users(self):
        print(self.__users)