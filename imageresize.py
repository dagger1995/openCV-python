#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2


# In[2]:


image=cv2.imread('sou.png',1)  


# In[ ]:


#give the dimension and show it 
dim = (400, 200)
 
# perform the actual resizing of the image and show it
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
cv2.imshow("resized", resized)
cv2.waitKey(0)


# In[ ]:





# In[ ]:





# In[ ]:




