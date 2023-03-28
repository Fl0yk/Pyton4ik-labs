NAME_ABBREVIATIONS = (r"\bMr\.", r"\bMrs\.", r"Dr\.", r"St\.", r"Blvd\.", r"Ave\.", r"Sq\.",
                      r"Rd\.", r"Bldg\.", r"B\.Sc\.", r"M\.A\.", r"Ph\.D\.", r"M\.D\.", r"LT\.")

OTHER_ABBREVIATIONS = (r"etc\.", r"Re\.", r"p\.", r"exp\.", r"err\.", r"et\.al\.", r"ex\.", 
                       r"e\.g\.", r"fin\.", r"i\.e\.", r"vs\.", r"N\.B\.", r"P\.S\.", r"P\.P\.S\.",
                       r"P\.S\.S\.", r"ft\.", r"oz\.", r"pt\.", r"in\.", r"sec\.", r"\bg\.",
                       r"cm\.", r"qt\.", r"p\.m\.")

NOT_ELEM = "No such elements"
ERROR_ADD = "Error when adding"
ERROR_INPUT = "Incorrect input. Please, try again:"
SAVE_CONTAINER = "You want save container?(y/n)"

K = 10

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
PATH = "/home/floyk/Рабочий стол/IGI-Labs/Pyton4ik-labs/lab_2/Files/" #os.path.abspath(__file__).replace("/constans.py", "/") + "Files/"
YES = "y"
NO = "n"
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
