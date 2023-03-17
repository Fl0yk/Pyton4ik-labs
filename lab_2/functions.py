import re
from constans import *
from my_container import Container, UsersAndContainers

def clear_text(text):
    word = re.sub(r'\"[\w\d\s,\'!?.]*[?!]\"\s[a-z]',"A,",text) #прямая речь - начало предложения, но с ! или ?
    word = re.sub(r', \"[\w\d\s,\'!?.]*[?!.]\"',".",word) #прямаяречь - конец предложения
    word = re.sub(r'\"[\w\d\s,\'!?.]*,\"','A,',word) #прямая речь - начало предложения
    word = re.sub(r'\"[\w\d\s,\'!?.]*[?!.]\"','A.',word) #прямая речь - отдельное предложение
    #print(word)
    word = re.sub(r"[A-Z]. [A-Z]. [A-Z]", " ", word)
    
    for abbr in NAME_ABBREVIATIONS:
        word = re.sub(abbr, " ", word)
    
    for abbr in OTHER_ABBREVIATIONS:
        word = re.sub(abbr + r"\s[A-Z]", ". ", word)
        word = re.sub(abbr, " ", word)
    
    word = re.sub(r"\w+\.\w+"," ", word)

    word = re.sub(r"\.\s\.\s\.",".", word)
    
    #print(word)

    return word

def amount_of_sent(text):
    return len(re.findall(r"[.!?]", clear_text(text)))

def non_dec_sent(text):
    return len(re.findall(r"[!?]", clear_text(text)))

def give_all_words(text):
    textik = re.sub(r"\b\d+e[+-]\d+|\b\d+[.,]?\d+|\b\d+"," ", text)
    textik = re.sub(r"[!.?\",']", " ", textik)
    return textik.split()

def averege_len_sent(text):
    count_sent = amount_of_sent(text)
    if(not count_sent):
        return 0
    len_words = 0
    
    for word in give_all_words(text):
        len_words += len(word)

    return round(len_words / count_sent)

def averege_len_word(text):
    len_words = 0
    all_words = give_all_words(text)
    if not len(all_words):
        return 0
    
    for word in all_words:
        len_words += len(word)
        
    return round(len_words / len(all_words))

def n_grams(text, n = 4):
    text = text.lower()
    words = give_all_words(text)
    ngrams = dict()
    
    for i in range(len(words) - n + 1):
        ngram = " ".join(words[i : i + n])
        
        if(ngram in ngrams):
            ngrams[ngram] += 1
        else:
            #ngrams = ngrams + {ngram : 1}
            ngrams[ngram] = 1
            
    
    return sorted(ngrams.items(), key = lambda x: x[1], reverse = True)

def menu():
    input_str = " "
    users_conteiners = UsersAndContainers()
    current_container = Container()
    
    print("Input your username")
    current_user = username_check(input())
    users_conteiners.add_user(current_user)
    current_container.load(users_conteiners.find_user(current_user))
    
    while(input_str != EXIT):
        input_str = input()
        func = input_str.split()[0]
        if(len(func) + 1 < len(input_str)):
            params = input_str[len(func) + 1::]
        else:
            params = " "
        
        if(func == ADD):
            current_container.add(params)
        elif (func == REMOVE):
            current_container.remove(params)
        elif (func == FIND):
            print(current_container.find(params))
        elif (func == LIST):
            current_container.list()
        elif (func == GREP):
            print(current_container.grep(params))
        elif (func == HELP_ME):
            print(HELP_COMMANDS)
        elif (func == LOAD):
            current_container.load(PATH + params)
        elif (func == SWITCH):
            print("You want save container?(y/n)")
            if(yes_no(input())):
                current_container.save(users_conteiners.find_user(current_user))
            print("Input your username")
            current_user = username_check(input())
            users_conteiners.add_user(current_user)
        elif (func == EXIT):
            print("You want save container?(y/n)")
            if(yes_no(input())):
                current_container.save(users_conteiners.find_user(current_user))
        print("----------------------------------\n")
            
                
def username_check(username : str):
    while(re.findall(r"[?!#$\"/\\\s]+", username)):
        print("Incorrect input. Please, try again:")
        username = input()
    return username

def yes_no(y_n : str):
    while(True):
        if(y_n == YES):
            return True
        elif (y_n == NO):
            return False
        print("Incorrect input. Please, try again:")
        y_n = input()