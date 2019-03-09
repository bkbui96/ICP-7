from nltk.stem import WordNetLemmatizer

txt = open("output.txt").read()

lemmatizer = WordNetLemmatizer()

for x in txt.split():
    print(lemmatizer.lemmatize(x, 'v'))