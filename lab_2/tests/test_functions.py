from Task1.functions import clear_text, amount_of_sent, non_dec_sent, give_all_words, averege_len_sent, averege_len_word, n_grams

def test_clear_text1():
    text = "A. A. Vovchik."
    print(clear_text(text))
    assert clear_text(text) == " ovchik."
    
def test_clear_text2():
    text = "\"Aaa. Aa! Aaaa,\" aaaa bb!"
    assert clear_text(text) == "A, aaaa bb!"
    
def test_clear_text3():
    text = "Aaaa. A. A. Aaaa bb. \"Bbb. Bb! Bbbb,\" aaa. \"Aaa! Aaaa.\" Bbbb aa.py."
    assert clear_text(text) == "Aaaa.  aaa bb. A, aaa. A. Bbbb  ."
    
def test_clear_text4():
    text = "Aaa aa aaaaa. Aaaa aaa? Aaaaaaaaa... Aaa aa aaa?"
    assert clear_text(text) == "Aaa aa aaaaa. Aaaa aaa? Aaaaaaaaa. Aaa aa aaa?"
    
def test_amount_sent1():
    text = "A aaa aa."
    assert amount_of_sent(text) == 1
    
def test_amount_sent2():
    text = "Aaa aa aaaaa. Aaaa aaa? Aaaaaaaaa... Aaa aa aaa?"
    assert amount_of_sent(text) == 4
    
def test_amount_sent3():
    text = ""
    assert amount_of_sent(text) == 0
    
def test_amount_sent4():
    text = "Aaaa. A. A. Aaaa bb. \"Bbb. Bb! Bbbb,\" aaa. \"Aaa! Aaaa.\" Bbbb aa.py."
    assert amount_of_sent(text) == 4
    
def test_non_dec_sent1():
    text = "A aaa aa."
    assert non_dec_sent(text) == 0
    
def test_non_dec_sent2():
    text = "Aaa aa aaaaa. Aaaa aaa? Aaaaaaaaa... Aaa aa aaa?"
    assert non_dec_sent(text) == 2
    
def test_non_dec_sent3():
    text = ""
    assert non_dec_sent(text) == 0
    
def test_non_dec_sent4():
    text = "Aaaa. A. A. Aaaa bb. \"Bbb. Bb! Bbbb,\" aaa. \"Aaa! Aaaa.\" Bbbb aa.py?"
    assert non_dec_sent(text) == 0
    
def test_all_words1():
    text = ""
    assert give_all_words(text) == []
    
def test_all_words2():
    text = "A aa aba"
    assert give_all_words(text) == ["A", "aa", "aba"]

def test_all_words3():
    text = "1e+20 dcd 1234 aa 12.35 gg"
    assert give_all_words(text) == ["dcd", "aa", "gg"]
    
def test_all_words4():
    text = "Aaaa. A. A. Aaaa bb. \"Bbb. Bb! Bbbb,\" aaa. \"Aaa! Aaaa.\" Bbbb aa.py?"
    assert give_all_words(text) == ["Aaaa", "A", "A", "Aaaa", "bb", "Bbb", "Bb", "Bbbb", "aaa",
                                    "Aaa", "Aaaa", "Bbbb", "aa", "py"]
    
def test_all_words():
    text = "Aaaaaaaaaa12! Bbeeww wworqwert rtyhr22? Ff3. . ."
    assert give_all_words(text) == ["Aaaaaaaaaa12", "Bbeeww", "wworqwert", "rtyhr22", "Ff3"]
    
def test_len_sent1():
    text = ""
    assert averege_len_sent(text) == 0
    
def test_len_sent2():
    text = "Aa. Ab. Ac. Ad. Ae. Af."
    assert averege_len_sent(text) == 2
    
def test_len_sent3():
    text = "Aaaaaaaaaa12! Bbeeww wworqwert rtyhr22? Ff3. . ."
    assert averege_len_sent(text) == 12
    
def test_len_word1():
    text = ""
    assert averege_len_word(text) == 0
    
def test_len_word2():
    text = "Aa. Ab. Ac. Ad. Ae. Af."
    assert averege_len_word(text) == 2
    
def test_len_word3():
    text = "Aaaa5. A. A. Aaaa5 bb3. \"Bbb4. Bb3! Bbbb5,\" aaa4. \"Aaa4! Aaaa5.\" Bbbb5 aa.py?"
    assert averege_len_word(text) == 4
    
def test_n_gramms1():
    text = ""
    assert n_grams(text) == []
    
def test_n_gramms2():
    text = "Aa. Ab. Ac. Ad. Ae. Af."
    assert n_grams(text, n = 2) == [("aa ab", 1), ("ab ac", 1), ("ac ad", 1), ("ad ae", 1), ("ae af", 1)]
    
def test_n_gramms3():
    text = "Ab ad ab ad ab ad aa"
    assert n_grams(text, n = 2) == [("ab ad", 3), ("ad ab", 2), ("ad aa", 1)]