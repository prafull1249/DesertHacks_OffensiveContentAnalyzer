# coding: utf-8

# ## Import Modules

# In[165]:

# import graphlab as gl
#from gensim.models import KeyedVectors as kv
from gensim.models import word2vec as wv
from gensim import models
import json
from textblob import TextBlob as tb
from textblob import Word
import csv
from nltk.corpus import stopwords

#Alchemy API imports 
import json
from watson_developer_cloud import AlchemyLanguageV1

alchemy_language = AlchemyLanguageV1(api_key='de1dd2eb1487d502de86cf8be3f814dbc721be7c')

model = models.Word2Vec.load_word2vec_format('data/GoogleNews-vectors-negative300.bin', binary=True) 
# ## Import Bag of Words

# In[191]:

with open("data/racialSlurWord.csv",'r') as file:
    bow_lines = file.readline()

bow = bow_lines.split(',')
with open("data/OffensiveWords.csv",'r') as file:
    bow_lines = file.readline()  

bow += bow_lines.split(',')
bow_updated = []
for word in bow:
    if word in model.vocab:
        bow_updated.append(word)
    # bow_updated.append(word)
bow = set(bow)

# ## Function to extract parts of speech

def extract_parts_of_speech(sentence):
    blob = tb(sentence.lower())
    extracted_words = []

    stop = set(stopwords.words('english'))
    for tag in blob.tags:
        #if tag[1]=='NN' or tag[1] == 'JJ' and tag[0] not in stop:
        if tag[0] not in stop:
            extracted_words.append(tag[0])
    lemmatized_words = lemmatize(extracted_words)
    return lemmatized_words


# ## Function to lemmatize words

def lemmatize(list_of_words):
    lemmatized_words = []
    for word in list_of_words:
        try:
            # This condition is because in some cases cuss and offensive words are 
            # lemmatized to ordinary words ex. ass->as
            if word not in bow:
                lem_word = Word(word).lemmatize()
            else:
                lem_word = word
        except UnicodeDecodeError:
            lem_word = Word(word.decode('unicode-escape')).lemmatize()
        lemmatized_words.append(lem_word)
    return lemmatized_words


# ## Function to expand word list using word2vec

# In[238]:

def expand_word_list(list_of_words):
    expanded_word_list = []
    for word in list_of_words:
        if word in model.vocab:
            word_2_vec_list = model.most_similar(word, topn=10)
            for word_tuple in word_2_vec_list:
                expanded_word_list.append(word_tuple[0])
    return expanded_word_list


# ## Find similarity

# In[239]:

def find_offensive_value(s):
    list_of_words = extract_parts_of_speech(s)
    print list_of_words
    expanded_list = expand_word_list(list_of_words)
    print expanded_list
    return model.n_similarity(expanded_list, bow_updated)


# In[248]:

def start(s):
    return find_offensive_value(s)


def get_api_result(s):
    value = find_offensive_value(s)
    api_result = alchemy_language.combined( text=s, extract='entities,keywords,doc-emotion, doc-sentiment', max_items=1)
    api_result["offensive_quotient"] = value
    return json.dumps(api_result, indent=2)

#if __name__ == '__main__':

def get_quotient(s):
    
    offensive_quotient = find_offensive_value(s)
    json_obj = alchemy_language.combined( text=s, extract='entities,keywords,doc-sentiment, ', sentiment=1, max_items=1)
    print(json.dumps( , indent=2))
    print offensive_quotient