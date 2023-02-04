#!/usr/bin/env python
# coding: utf-8

# In[1]:



import pathlib
import re
import pickle


# In[2]:


# create person class
class Person:
    #define and initialize variables of person
    def __init__(self, last, first, mi, id, phone):
        self.last=last
        self.first = first
        self.mi = mi
        self.id = id
        self.phone = phone
    def getset(self):
        print("ID: ". self.id)
        print("First Name: ", self.first )
        print("Middle Initial: ", self.mi)
        print("Last Name", self.last)
        print("Phone Number: ", self.phone)
        
        
        
        
  


# In[8]:





# In[ ]:





# In[3]:


def process(f,pdict):
    iter = 0
    idre = '[A-Za-z][A-Za-z]\d{4}'
    phonere= '\d{3}-\d{3}-\d{4}'
    
    for line in f:
        if (iter == 0):
            iter+=1
            continue
        
        # process name
        list = line.split(',')
        print(list)
        list[0] = list[0].capitalize()
        ln = list[0]
        list[1] = list[1].capitalize()
        fn = list[1]
        if (list[2] == ''):
            list[2] = 'X'
        else:
            list[2] = list[2].capitalize()
        mi=list[2]
    
        # process id
        while(True):
            if (re.match(idre, list[3])==None):
                print("Re enter id with pattern: 2 letters, 4 digits\n")
                list[3] = input("Enter new ID: ")
            else:
                break
        id=list[3]
        #process phone number
        while(True):
            if(re.match(phonere, list[4]) == None):
                print("Re enter phone number with pattern: 3 digits-3 digits-4 digits")
                list[4] = input("Enter new Phone Number: ")
            else:
                break
                
        pn=list[4]

        newperson = Person(fn,ln,mi,id,pn)
        pdict[id] = newperson
        print(list)
        
    return(pdict)
    
    
    
    


# In[4]:


def main():
    #create a dict for each person
    import os
    import sys
    path = sys.argv[1]
    while(True):
        if os.path.exists(path):
            break
        else:
            print("File does not exist")
    
    dict = {}
    file = open(path, 'r', encoding='utf-8')
    dict = process(file,dict)
    file.close()


# In[6]:


main()
        


# In[ ]:


if __name__ == "__main__":
    main()
    

