import random
words_file = 'valid-wordle-words.txt'
with open(words_file,'r') as f:
    words = f.readlines()
    print(random.choice(words).strip())