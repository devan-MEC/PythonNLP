
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize,word_tokenize

ps=PorterStemmer()
example_words=["python","pythoner","pythoning","pythoned","pythonist"]
for i in example_words:
    print(ps.stem(i))#strips each element i in example_words to its stem
print('----------------------------------------------')
new_text="It is important to be very pythonly while you are pythoning your code"
words=word_tokenize(new_text)#tokenizes new_text into words
for j in words:
    print(ps.stem(j))#stripping each element in words to its stem
