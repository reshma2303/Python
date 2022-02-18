#!/usr/bin/env python
# coding: utf-8

# In[100]:


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as mp
import pandas as pd


# ## PART 1 

# #### Get all datasets

# In[101]:


sns.get_dataset_names()


# #### Load Penguins dataset

# In[102]:


df=sns.load_dataset('penguins')
df.head()


# #### Drop Null Records

# In[103]:


df1 = df.dropna()
df1


# #### Count of records which were dropped

# In[104]:


print("No of records dropped",len(df)-len(df1))


# #### Create a column which number of penguins on each island

# In[105]:


df1['penguin_count'] = df1['island'].groupby(df1['island']).transform('count')
df1


# #### Create a column which has mean bill length of each species

# In[106]:


df1['mean_bill_length'] = df1['bill_length_mm'].groupby(df1['species']).transform('mean')
df1


# ## Part 2

# #### Create a column which has the weighted mean of bill length and bill depth of species
# #### bill length weight=0.7 and bill depth weight=0.3

# #### weighted mean= (w1*n1+w2*n2) / (w1+w2)

# In[107]:


def add_weighted_mean_column(row,w_length=0.7, w_depth=0.3):
    return (w_length * row['bill_length_mm'] + w_depth * row['bill_depth_mm'])/2
    
    
df1['bill_weighted_mean'] = df1.apply(lambda row: add_weighted_mean_column(row), axis=1)


# In[108]:


df1


# ## Part 3

# #### Plot a scatter plot with bill length on x and bill depth on y where the color of points is the species and style is the island

# In[109]:


sns.scatterplot(data=df1, x="bill_length_mm", y="bill_depth_mm", hue="species", style="island")
plt.plot([35,60],[13.5,19],linewidth=2)
plt.plot([34,53],[14,21.5],linewidth=2)

