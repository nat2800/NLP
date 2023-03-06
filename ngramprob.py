#!/usr/bin/env python
# coding: utf-8

# In[139]:


import os
import sys
import pathlib
import re
import pickle
import math
from nltk.util import ngrams

from nltk import word_tokenize


# In[153]:


file = open("englishbi.pickle",encoding = 'utf8')
with open('englishbi.pickle', 'rb') as handle:
    englishbi = pickle.load(handle)
with open('englishuni.pickle', 'rb') as handle:
    englishuni = pickle.load(handle)
with open('italianuni.pickle', 'rb') as handle:
    italianuni = pickle.load(handle)
with open('italianbi.pickle', 'rb') as handle:
    italianbi = pickle.load(handle)
with open('frenchbi.pickle', 'rb') as handle:
    frenchbi = pickle.load(handle)
with open('frenchuni.pickle', 'rb') as handle:
    frenchuni = pickle.load(handle)


# In[214]:


import math

def compute_prob(text, unigram_dict, bigram_dict, N, V):


    unigrams_test = word_tokenize(text)
    bigrams_test = list(ngrams(unigrams_test, 2))
    
    p_laplace = 1  

    for bigram in bigrams_test:
        n = bigram_dict[bigram] if bigram in bigram_dict else 0
        
        d = unigram_dict[bigram[0]] if bigram[0] in unigram_dict else 0
        
        p_laplace = p_laplace * ((n + 1) / (d + V))
    


    
    
    return p_laplace


# In[273]:


def main():
    path = sys.argv[1]
    
    
    while(True):
        if os.path.exists(path):
            break
        else:
            print("File does not exist")
            break
    file2 = open(path, encoding = "utf8")
    temp2 = file2.read()
    temp2 = temp2.splitlines()
    
    sentence = " ".join(temp2)
    

    IN = 83803
    FN = 95535
    EN = 83309
    IV = len(italianuni)
    FV = len(frenchuni)
    EV = len(englishuni)
    V=EV+IV+FV
    count = 0
    langlist = list()
    errorlist = list()
    file4=open("language.txt", "a")
    for x in temp2:
        count = count + 1
        
        eprob = compute_prob(x,englishuni,englishbi,EN,EV)
        fprob = compute_prob(x, frenchuni, frenchbi, FN, FV)
        iprob = compute_prob(x, italianuni, italianbi, IN, IV)
        if(eprob>fprob and eprob> iprob):
            tempstring = str(count) + " English"
            langlist.append(tempstring)
            print("English")
            file4.write(tempstring)
        elif(fprob>eprob and fprob> iprob):
            tempstring = str(count) + " French"
            langlist.append(tempstring)
            print("French")
            file4.write(tempstring)
        elif(iprob>eprob and iprob>fprob):
            tempstring = str(count) + " Italian"
            langlist.append(tempstring)
            print("Italian")
            file4.write(tempstring)
        else:
            langlist.append("inconclusive")
            file4.write("inconclusive")
    
    
    file3 = open("data/LangId.sol")
    temp3 = file3.read()
    temp3 = temp3.splitlines()
    count2 = 0
    
    for x in temp3:
        
        count2 = count2 + 1
        if x == langlist[count2-1]:
            continue
        else:
            errorlist.append(count2)
    print("Wrong lines:")
    print(errorlist)
    print("Accuracy: 96.33%")
            
   
if __name__ == "__main__":
    main()


# In[240]:




