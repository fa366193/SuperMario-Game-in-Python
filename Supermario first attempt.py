#!/usr/bin/env python
# coding: utf-8

# In[14]:


get_ipython().run_line_magic('matplotlib', 'inline')

from skimage.io import imread
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from IPython.html.widgets import interact
from IPython.display import YouTubeVideo, HTML

plt.rcParams.update(**{'figure.figsize':(8,6),
                       'figure.dpi':500,
                       'font.size':12})


# In[15]:


YouTubeVideo('cTiJaWCaKas')


# In[ ]:


data = pd.read_csv('Desktop/mario_data.csv')
df = pd.read_csv('Desktop/timelines.csv')
df.head()


# In[16]:


# Determining how long each player takes to finish
df.finaltime.hist(fc='#575757')
plt.xlabel("Time to finish level (s)")


# In[17]:


#Creating the path through the level
plt.plot(df.x, -df.y, '.k', alpha=0.3)
x = plt.xlim(0, 100)


# In[ ]:


#Restacking timelines so each run_id is a row
timelines = df.set_index(['run_id', 'time']).unstack()
timelines.head()


# In[18]:


#plotting path on top of an image of the level

plt.figure(figsize=(25, 15), dpi=200)
im = imread('Desktop/background.jpg')
im = im[:, :2000]
plt.imshow(im, origin='upper')

plt.plot(df.x * 16, df.y * 16, '.k', alpha=0.3)
plt.xlim(0, 1000)


# In[19]:


im = imread('Desktop/background.jpg')

def explore(run, time):
    # show path of a single run (red line), emphasizing a particular timestamp (black dot)
    plt.figure(figsize=(15, 7), dpi=100)
    ax = plt.gca()
    
    show_image(ax)
    draw_timeline(ax, run, time)
    
def show_image(axes):
    axes.imshow(im, interpolation='nearest', origin='upper', extent=[0, im.shape[1] / 16., im.shape[0] / 16., 0])    
    axes.set_xlim(0, 75)
    axes.set_ylim(14, -5)

def draw_timeline(axes, run, time):
    sub = timelines.iloc[run]
    x = sub.x
    y = sub.y
    
    xt = x.values[time]
    yt = y.values[time]
    
    axes.plot(x, y, 'r-',        # plot the timeline
             [xt], [yt], 'ko',   # overplot the black circle
             lw=3, ms=20)


# In[20]:


explore(run=5, time=20)


# In[21]:


# make run and time interactive parameters
interact(explore, run=(0, 110), time=(0, 350))


# In[ ]:




