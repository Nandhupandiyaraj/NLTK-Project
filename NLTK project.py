#!/usr/bin/env python
# coding: utf-8

# In[30]:


import nltk


# In[31]:


nltk.download()


# In[32]:


nltk.download('stopwords')


# In[33]:


nltk.download('punkt')


# In[34]:


from nltk import word_tokenize


# In[35]:


from nltk import sent_tokenize


# In[36]:


sentence = ('Hi there ! This is my world.')


# In[37]:


word_tokenize(sentence)


# In[38]:


sent_tokenize(sentence)


# In[39]:


from nltk.corpus import stopwords


# In[40]:


stopwords.fileids()


# In[41]:


stop = stopwords.words('english')
stop


# In[42]:


meaning_full_words = []
for w in word_tokenize(sentence):
    if w not in stop:
        meaning_full_words.append(w)
meaning_full_words


# In[43]:


from sklearn.feature_extraction.text import CountVectorizer

sentences = [
    "He like ice cream cream cream",
    "She likes ice cream",
    "Both of them likes ice cream"
]

cv = CountVectorizer(stop_words='english').fit(sentences)
cv

cv.vocabulary_

X = cv.fit_transform(sentences)

print(X.toarray())


# In[ ]:




