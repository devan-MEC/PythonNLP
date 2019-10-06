from nltk.tokenize import word_tokenize
from nltk import pos_tag
import nltk

#define chunking function text and regular expression representing grammar as parameter
def chunking(text,grammar):
    word_tokens=word_tokenize(text)

    #label words with part of speech
    word_pos=pos_tag(word_tokens)

    #create a chunk parser using grammar
    chunkParser=nltk.RegexpParser(grammar)

    #test it on the list of word tokens with tagged pos
    tree =chunkParser.parse(word_pos)

    for subtree in tree.subtrees():
        print(subtree)

    tree.draw()


text="I am Sahana working in Novitech in emb dept"
grammar="NP: {<DT>?<JJ>*<NN>}"
chunking(text,grammar)
