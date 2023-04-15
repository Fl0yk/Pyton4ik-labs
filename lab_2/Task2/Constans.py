from enum import Enum
import os

PATH = "Files/Containers/"
INVALID_REGEX = "Bad regular expression"
NOT_ELEM = "No such elements"
ERROR_ADD = "Error when adding"
ERROR_INPUT = "Incorrect input. Please, try again:"
SAVE_CONTAINER = "You want save container?(y/n)"
YES = "y"
NO = "n"

class COMMANDS(Enum):
    ADD = "add"
    REMOVE = "remove"
    EXIT = "exit"
    FIND = "find"
    GREP = "grep"
    LIST = "list"
    SAVE = "save"
    LOAD = "load"
    SWITCH = "switch"
    HELP = "help"
    #PATH = "/home/floyk/Рабочий стол/IGI-Labs/Pyton4ik-labs/lab_2/Files/" #os.path.abspath(__file__).replace("/constans.py", "/") + "Files/"
    HELP_ME = "help"


HELP_COMMANDS = "add <key> - add one element\n\
    remove <key> - delete key from container\n\
    find <key> - print a element if it has found it\n\
    list - print all elements of container\n\
    grep <regex> - check the value by regular\n\
    switch - switches to another user\n\
    load - load container from file\n\
    save - save container\n\
    exit - exit from programm\n"