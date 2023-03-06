#!/usr/bin/env python
# coding: utf-8

# In[34]:



import os
import sys
import nltk
import pathlib
import re
import pickle
from nltk import word_tokenize

nltk.download('punkt')


# In[23]:





# In[49]:


def gram_dicts(filepath):
    file = open(filepath, encoding='utf8')
    temp=file.read()
    temp = temp.splitlines()
    
    sentence = " ".join(temp)
 

    unigrams = word_tokenize(sentence)
    unigram_dict = {t:unigrams.count(t) for t in set(unigrams)}

    
    bigrams = [(unigrams[k], unigrams[k+1]) for k in range(len(unigrams)-1)]
    
    bigram_dict = {b:bigrams.count(b) for b in set(bigrams)}
    
    file.close()
    return unigram_dict, bigram_dict

    


# In[48]:





# In[40]:


def main():
    
            
    
    eng = input("Enter English Filepath: ")
    while(True):
        if os.path.exists(eng):
            break
        else:
            print("File doesn't exist")
            break
    
    uni, bi = gram_dicts(eng)
    with open('englishuni.pickle', 'wb') as handle:
        pickle.dump(uni, handle)
    with open('englishbi.pickle', 'wb') as handle:
        pickle.dump(bi, handle)
    
    fre = input("Enter French Filepath: ")
    while(True):
        if os.path.exists(fre):
            break
        else:
            print("File doesn't exist")
            break
    
    uni, bi = gram_dicts(fre)
    with open('frenchuni.pickle', 'wb') as handle:
        pickle.dump(uni, handle)
    with open('frenchbi.pickle', 'wb') as handle:
        pickle.dump(bi, handle)
        
    
    
    
            
            
    ita = input("Enter Italian Filepath: ")
    while(True):
        if os.path.exists(ita):
            break
        else:
            print("File doesn't exist")
            break
    
    uni, bi = gram_dicts(ita)
    with open('italianuni.pickle', 'wb') as handle:
        pickle.dump(uni, handle)
    with open('italianbi.pickle', 'wb') as handle:
        pickle.dump(bi, handle)
    
    
if __name__ == "__main__":
    main()

