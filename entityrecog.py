from nltk.tokenize import word_tokenize
from nltk import pos_tag,ne_chunk

def named_entity_recognition(text):
    #tokenize the text
    word_tokens=word_tokenize(text)
    
    #pos( part of speech) tagging of word
    word_pos=pos_tag(word_tokens)

    #tree of word entities
    print(ne_chunk(word_pos))


text="Ben works for FlipKart so he went to London for a meeting"
named_entity_recognition(text)

