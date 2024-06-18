#!/usr/bin/env python
# coding: utf-8

# In[2]:


# NAMA : HERI SANTOSO
# CLASS : BYMAX


# In[3]:


# import libraries


# In[20]:


import requests
from bs4 import BeautifulSoup
import pickle


# In[34]:


def url_to_transcript(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page,'lxml')
    text = [p.text for p in soup.find_all('div', class_ = 'elementor-widget-theme-post-content')]
    print(url)
    return text


# In[35]:


urls = ['https://scrapsfromtheloft.com/movies/spider-man-no-way-home-transcript/',
      'https://scrapsfromtheloft.com/movies/fast-furious-9-transcript/',
      'https://scrapsfromtheloft.com/tv-series/money-heist-s05e01-end-of-the-road-transcript/',
      'https://scrapsfromtheloft.com/movies/eternals-2021-transcript/',
      'https://scrapsfromtheloft.com/comedy/venom-let-there-be-carnage-transcript/',
      'https://scrapsfromtheloft.com/comedy/shang-chi-legend-of-ten-rings-transcript/',
      'https://scrapsfromtheloft.com/tv-series/the-flash-s07e16-pow-transcript/',
      'https://scrapsfromtheloft.com/movies/joker-how-about-another-joke-murray-transcript/',
      'https://scrapsfromtheloft.com/movies/wonder-woman-1984-transcript/']


# In[36]:


movies = ['spiderman', 'fast and furious', 'money heist', 'eternals',
         'venom', 'sang chi', 'the flash', 
          'the flash', 'wonder woman']

# 1. fast and forious = karna filmnya ratingnya tinggi
# 2. money hesit = so basicly suka sama genre action yg ada mix economic financialnya gitu


# In[37]:


transcripts = [url_to_transcript(i) for i in urls ]


# In[39]:


get_ipython().system('mkdir transcripts ')

for i, c in enumerate(movies):
    with open('transcripts/' + c + 'txt', 'wb') as file:
        pickle.dump(transcripts[i],file)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




