import re
from constans import NAME_ABBREVIATIONS, OTHER_ABBREVIATIONS

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