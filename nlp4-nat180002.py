#!/usr/bin/env python
# coding: utf-8

# In[11]:


import nltk
nltk.download('treebank')
nltk.download('webtext')
nltk.download('nps_chat')
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

import os
import sys
import pathlib
import re
import pickle
from random import seed
from random import randint
from nltk.book import *
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk import sent_tokenize
from nltk.stem import WordNetLemmatizer


# In[2]:


def game(common_words):
    seed = 123
    points = 5
    mystery = common_words[randint(0, 49)]
    guess =[]
    char=[*mystery]
    
    for t in char:
        guess.append('_')
    while(points >=0):
        for t in guess:
            print(t)
        templetter=input("Guess a letter: ")
        if(templetter == '!'):
            print("Game Over")
            break;
        temp2 = 0
        count3 = 0
        for t in char :
            if (templetter ==t):
                guess[count3] = templetter
                temp2 = temp2 +1
            count3 = count3 + 1
        if temp2 == 0:
            points = points - 1
    print("Game Over")
        
         
        


# In[8]:


def preprocess(filepath):
    file = open(filepath)
    temp = file.read().splitlines()

    sentence = " ".join(temp)
    sentence

    tokens = sentence.split()
    tokens = word_tokenize(sentence)
    print(tokens)
    tokens4 = [t.lower() for t in tokens]

    
    set4 = set(tokens4)
    


    #3a.
    tokens4 = [t for t in tokens4 if t.isalpha() and
           t not in stopwords.words('english') and len(t)>5]

    
    
    #3b.
    wnl = WordNetLemmatizer()
    lemmas = [wnl.lemmatize(t) for t in tokens4]
    # make unique
    lemmas_unique = list(set(lemmas))  # ?
    print("\nThe number of unique lemmas in text4: ", len(lemmas_unique))


    sentence2 = " ".join(lemmas_unique)
    #3c.
    tokens5 = nltk.word_tokenize(sentence2)
    tags = nltk.pos_tag(tokens5)
    tags[1:20]
    #3d.
    nountag = []
    counter = 0
    for t in tags:
        if(tags[counter][1] == 'NN' or tags[counter][1] == 'NNP' or tags[counter][1] == 'NNS' or tags[counter][1] == 'NNPS' ):
            nountag.append(tags[counter])
        counter = counter+1
    nountag
    nouns = []
    counter2 = 0
    for t in nountag:
        nouns.append(t[0])
    #3e.

    print(len(tokens4))
    print(len(nountag))

    #(return these in function)
    dict = {t:tokens4.count(t) for t in nouns}

    sorted_dict = sorted(dict.items(), key=lambda x:x[1], reverse=True)
    print(sorted_dict[0:50])

    common_words = []


    for t in range(0,50):
        common_words.append(sorted_dict[t][0])
    return common_words


# In[10]:


def main():
        
        path = sys.argv[1]
        while(True):
            if os.path.exists(path):
                break
            else:
                print("File doesn't exist")
                break
        common = preprocess(path)
        game(common)

if __name__ == "__main__":
     main()

