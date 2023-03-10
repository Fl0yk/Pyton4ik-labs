import re
from constans import abbreviations

def clear_text(text):
    word = re.sub(r', \"[\w\d\s,\'!?]*[?!.]\"',".",text) #прямаяречь - конец предложения
    word = re.sub(r'\"[\w\d\s,\'!?]*,\"','A,',word) #прямая речь - начало предложения
    word = re.sub(r'\"[\w\d\s,\'!?]*[?!.]\"','A.',word) #прямая речь - отдельное предложение

    for abr in abbreviations:
        word = re.sub(abr,re.sub(r"\."," ",abr),word)

    word = re.sub(r"\w+\.\w+"," ", word)

    word = re.sub(r"[A-Z]. [A-Z]. [A-Z]", " ", word)

    word = re.sub(r"\.\s\.\s\.",".",word)

    return len(re.findall(r"[.!?]", word))
    

def give_all_words(text):
    pass

def word_separation(word):
    if(word is not str):
        return
    
    word = word[word.startswith("\""):len(word) - word.endswith("\""):]