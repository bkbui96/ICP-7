import nltk

txt = open("output.txt").read()

stokens = nltk.sent_tokenize(txt)

for s in stokens:
    print(s)