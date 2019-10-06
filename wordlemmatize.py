from nltk.stem import WordNetLemmatizer
le=WordNetLemmatizer()
#Used to lemmatize(group together words meaning the same thing)
print(le.lemmatize("cats",pos="a")) #pos= Parts Of Speech,a denotes adjectives,v denotes verbs etc (i.e  parts of speech)

print(le.lemmatize("cacti",pos="a"))


print(le.lemmatize("goes",pos="a"))
print(le.lemmatize("rocks",pos="a"))
print(le.lemmatize("python",pos="a"))
print(le.lemmatize("better",pos="a")) #gets replaced with good since it means the same

print(le.lemmatize("gone",pos="v"))
