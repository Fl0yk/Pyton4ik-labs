from functions import amount_of_sent, non_dec_sent, averege_len_word, averege_len_sent, n_grams, menu
from constans import K, PATH
from my_container import Container, UsersAndContainers
import re
with open('test_file.txt') as f:
    text = f.read()
print(text)

count = amount_of_sent(text)
print(f"amount of sentences in the tex: {count}")

print(f"amount of non-declarative sentences in the tex: {non_dec_sent(text)}")

print(f"average length of the sentence in characters (words count only): {averege_len_sent(text)}")

print(f"average length of the word in the text in characters: {averege_len_word(text)}")

print(f"top-{K} repeated 2-grams in the text:")
for gram in n_grams(text, n = 2)[:K]:
    print(gram)
    
    
print("--------------------------------------------\nTask 2\n-------------------------------------------------------\n")

menu()