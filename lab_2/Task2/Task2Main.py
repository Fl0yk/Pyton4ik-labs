import os
from Task2.Constans import COMMANDS, ERROR_INPUT, SAVE_CONTAINER, HELP_COMMANDS, PATH
from Task2.functions import username_check, yes_no
from Task2.my_container import UsersAndContainers, Container


def task2Main():
    input_str = ""
    users_conteiners = UsersAndContainers()
    current_container = Container()
    
    print("Input your username")
    current_user = username_check(input())
    users_conteiners.add_user(current_user)
    
    print("You want load container?(y/n)")
    if(yes_no(input())):
        current_container.load(users_conteiners.find_user(current_user))
    
    while (True):
        input_str = input()
        if (input_str.isspace() or input_str == ""):
            print(ERROR_INPUT)
            continue
        
        func = input_str.split()[0]
        if(len(func) + 1 < len(input_str)):
            params = input_str[len(func) + 1::]
        else:
            params = ""
        
        match func:
            case COMMANDS.ADD._value_:
                current_container.add(*params.split())
                
            case COMMANDS.REMOVE._value_:
                current_container.remove(params)
                
            case COMMANDS.FIND._value_:
                print(current_container.find(*params.split()))
                
            case COMMANDS.SAVE._value_:
                current_container.save(users_conteiners.find_user(current_user))
                
            case COMMANDS.LIST._value_:
                current_container.list()
                
            case COMMANDS.GREP._value_:
                print(current_container.grep(params))
                
            case COMMANDS.HELP_ME._value_:
                print(HELP_COMMANDS)
            case COMMANDS.LOAD._value_:
                if params:
                    current_container.load(os.path.join(PATH, params + "Container.txt"))     #PATH + params + "Container.txt"
                else:
                    current_container.load(users_conteiners.find_user(current_user))
                    
            case COMMANDS.SWITCH._value_:
                print(SAVE_CONTAINER)
                if (yes_no(input())):
                    current_container.save(users_conteiners.find_user(current_user))
                print("Input your username")
                current_user = username_check(input())
                users_conteiners.add_user(current_user)
                del current_container
                current_container = Container()
                print("You want load container?(y/n)")
                if (yes_no(input())):
                    current_container.load(users_conteiners.find_user(current_user))
                    
            case COMMANDS.EXIT._value_:
                print(SAVE_CONTAINER)
                if(yes_no(input())):
                    current_container.save(users_conteiners.find_user(current_user))
                return
        print("----------------------------------\n")