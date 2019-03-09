from nltk.stem import PorterStemmer
import nltk

txt = open("output.txt").read()

pStemmer = PorterStemmer()

for x in txt.split():
    print(pStemmer.stem(x))
