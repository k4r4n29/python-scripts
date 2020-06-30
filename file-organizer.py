#!/usr/bin/env python
# coding: utf-8

# In[16]:


import os
import shutil
path = input("Enter your path to the directory to be organized => ")

list_ = os.listdir(path)
# print(list_)

for file_ in list_:
    name,ext = os.path.splitext(file_)
#     print(name,ext)
    ext = ext[1:]
    if ext == '':
        continue
    if os.path.exists(path+'/'+ext): 
            shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_) 
    else: 
        os.makedirs(path+'/'+ext) 
        shutil.move(path+'/'+file_, path+'/'+ext+'/'+file_)
print(f"path => {path} organized")


# In[ ]:




