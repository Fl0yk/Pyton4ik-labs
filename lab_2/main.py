from functions import clear_text
import re
with open('lab_2/test_file.txt') as f:
    text = f.read()
print(text)

count = clear_text(text)
print(f"amount of sentences in the tex: {count}")