#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


#understanding of numpy arrays 
np.zeros((400,300))


# In[3]:


np.full((400,300),255)


# In[4]:


#gan library for face recognition
get_ipython().system('pip3 install opencv-contrib-python')


# In[24]:


import cv2
#only for collab
#import matplotlib.pyplot as plt 


# In[25]:


print(cv2.__version__)


# In[26]:


#image reading 
img=cv2.imread('index.jpeg',1)  
#1 means same colour channel  ----
#0 means no colour ----
#-1 maintain image transparency ---
#split into BGR


# In[31]:


#print shape 
img.shape


# In[20]:


# opencv suppert BGR 
# type of img
type(img)


# In[ ]:


#to display image
cv2.line(img,(0,0),(100,30),(0,0,255),3)    # to display line on the image 
cv2.imshow('index',img)
cv2.waitKey(0)


# In[ ]:


# wait fro window to close
cv2.waitKey(0)    #mili/micro sec
# to  stop image editor


# In[ ]:


# only for matplotlib
#plt.imshow()


# In[ ]:


#from google.colab.patches import cv2_imshow


# In[ ]:


#plt.imshow('coffee',img)


# In[ ]:


#to draw a line in image

