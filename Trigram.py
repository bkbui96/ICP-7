from nltk import ngrams

txt = open("output.txt").read()

n = 3
tri = ngrams(txt.split(), n)

for x in tri:
    print(x)