import nltk

txt = open("output.txt").read()

words = nltk.word_tokenize(txt)
words=[word.lower() for word in words if word.isalpha()]

for w in words:
    print(w)