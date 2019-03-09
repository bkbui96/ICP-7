from nltk import wordpunct_tokenize, pos_tag, ne_chunk

txt = open("output.txt").read()

print(ne_chunk(pos_tag(wordpunct_tokenize(txt))))