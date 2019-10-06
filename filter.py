from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

example_sent="this is a sample sentence! demonstrating the power of stopwords and tokenizing"
stop_words=set(stopwords.words('english'))#stores useless words in stop_words
word_tokens=word_tokenize(example_sent)#stores all the words,characters in example_sent to word_tokens in the form of an array
filtered_sentence={w for w in word_tokens if not w in stop_words  }#list comprehension to store store all 'useful' words from word_tokens  to list filtered_sentence ignoring 'unimportant' words
print(stop_words)
print(word_tokens)
print(filtered_sentence)

