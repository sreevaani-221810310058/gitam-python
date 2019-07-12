#!/usr/bin/env python
# coding: utf-8

# #standard libraries#
# . file i/o
# . regular expression
# . datetime
# . math(numerical and mathematical)
# 

# ### file handling in python
# - file:- document containing information resides on the permanenet storage
# - different types of files:- txt,doc,pdf,csv and etc...
# - input--keyboard
# - output--file
# ### modes of the file
# - 'w'--this mode is used to writing files
#  -- if the file is not present first it creates the file and write so me data to it
#  -- if the file is already present the it will rewrite the new content 

# In[3]:


# function to create a file and write to the file
def createfile(filename):
    f=open(filename,'w')
    for i in range(10):
        f.write('this is %d line\n'%i)
    print("file is created and data has written")
    return
createfile('file1.txt')
    


# In[4]:


pwd


# In[5]:


ls


# In[10]:


def createfile(filename):
    f=open(filename,'w')
    f.write('testing...\n')
    print("file is created and data has written")
    return
createfile('file1.txt')
    


# In[11]:


cat file1.txt


# In[8]:


def createfile(filename):
    f=open(filename,'w')
    for i in range(10):
        f.write('this is %d line\n'%i)
    print("file is created and data has written")
    return
createfile('file1.txt')
    


# In[9]:


cat file1.txt


# In[18]:


def appenddata(filename):
    f=open(filename,'a')
    for i in range(10):
        f.write("this is %d line\n"%i)
    print("file is created and data has written")
    return
appenddata('file2.txt')
    


# In[19]:


cat file2.txt


# In[22]:


def appenddata(filename):
    f=open(filename,'a')
    f.write('new line \n')
    f.write('new line 1\n')
    print("file is created and data has written")
    return
appenddata('file2.txt')


# In[23]:


cat file2.txt


# In[26]:


# function to read the file data
def readfiledata(filename):
    f=open(filename,'r')
    if f.mode=='r':
        x=f.read()
        print(x)
    f.close()
    return
readfiledata('file2.txt')


# In[ ]:


def fileoperations(filename,mode):
    with open(filename,mode) as f:
        if f.mode == 'r':
            data=f.read()
            print(data)
        elif f.mode=='a':
            f.write('data to the file')
            print('the data successfully written')
    f.close()
    return
filename=input('enter the filename')
mode=input('enter the mode of the filename')
fileoperations(filename,mode)


# In[42]:


cat ss


# In[36]:


# data analysis
# word count program
def wordcount(filename,word):
    with open(filename,'r') as f:
        if f.mode == 'r':
            x=f.read()
            li=x.split() # its splits the string with whitespace
    cnt = li.count(word)
    return cnt
filename=input('enter the filename:')
word=input('enter the word:') # which word count you need
wordcount(filename,word)


# In[4]:


def fileoperations(filename,mode):
    with open(filename,mode) as f:
        if f.mode=='r':
            data=f.read()
patterns (RE) represents set of the values -(0-9) any digits
            print(data)
        elif f.mode=='a':
            f.write('data to the file')
            print('the data successfully written')
    f.close()
    return
filename=input('enter the filename')
mode=input('enter the mode of the filename')
fileoperations(filename,mode)


# In[6]:


# charcter count from the file
def charcount(filename):
    with open(filename,'r') as f:
        if f.mode == 'r':
            x=f.read()
            li=list(x) 
    return len(li)
filename=input('enter the filename:')
character(filename)


# In[7]:


s1="python programming"
print(s1.split('a'))


# In[34]:


# function to find the number of lines
# input ---filename(file2.txt)
# output --no of lines(3)

def linescount(filename):
    with open(filename,'r') as f:
        if f.mode == 'r':
            x=f.read()
            li=x.split("\n
patterns (RE) represents set of the values -(0-9) any digits") 
    return len(li)
filename=input('enter the filename:')
linescount(filename)


# In[23]:


#print the lower and upper characters
def casecount(filename):
    cntupper=0
    cntlower=0
    with open(filename,'r') as f:
        if f.mode == 'r':
            x=f.read()
            li=list(x)
    for i in li:
        if i.isupper():
            cntupper += 1
        elif i.islower():
            cntlower += 1
    output ='upper case ={0},lower case ={1}'.format(cntupper,cntlower)
    return output
filename=input('enter the filename:')
casecount(filename)


# ### math, random, os
# - os package it contains the certain methods which works with os
# 
# 

# In[26]:


ls


# In[32]:


cd desktop/pythonprog


# In[35]:


import os
os.listdir()


# In[36]:


li=os.listdir('Desktop')
for i in li:
    print(i)


# - older version of python --os.listdir()
# - newversion python -- os.scandir() and pathlib.path()

# In[ ]:


from pathlib import path
li


# # listing all the files in the directory

# In[39]:


import os
dirpath ="Desktop"
for i in os.listdir(dirpath):
    if os.path.isfile(os.path.join(dirpath,i)):
        print(i)


# In[41]:


dirpath= 'Desktop'
with os.scandir(dirpath) as f:
    for i in f:
        if i.is_file():
            print(i.name)


# In[42]:


pwd


# ## listing of the subdirectories

# In[47]:


from pathlib import Path
dirpath=Path('Desktop')
for i in dirpath.iterdir():
    if i.is_dir():
        print(i.name)


# In[48]:


os.mkdir('single directory')


# In[49]:


import pathlib
p= pathlib.Path('testfolder')
p.mkdir()


# In[50]:


ls


# ### create multiple directories

# In[61]:


import os
os.makedirs('shivani/gitam/')


# In[62]:


ls


# In[66]:


import os
dirpath ='Desktop'
for f_name in os.listdir(dirpath):
    if f_name.endswith('.html'):
        print(f_name)


# ## deleting files and directory

# In[67]:


ls


# In[68]:


cat data.txt


# In[70]:


import os
data_file='file1.txt'
os.remove(data_file)


# In[71]:


ls


# In[72]:


data_dir ='testfolder'
os.rmdir(data_dir)


# In[73]:


ls


# In[74]:


import shutil
data_dir ='2019'
shutil.rmtree(data_dir)


# In[75]:


ls


# ### REGUALR EXPRESSIONS

# - USED to specific pattern matching
# - symbolic notations of pattern
#   - patterns (RE) represents set of the values 
# -(0-9) any digits
# 

# regex

# In[ ]:




