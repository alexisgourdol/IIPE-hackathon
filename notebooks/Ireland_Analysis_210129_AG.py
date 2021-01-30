# -*- coding: utf-8 -*-
# <nbformat>4</nbformat>

# <markdowncell>

# # Preprocessing from package

# <markdowncell>

# ## Imports packages and sample .txt

# <markdowncell>

# Checking virtualenv with `pyenv`

# <codecell>

!pyenv virtualenvs

# <markdowncell>

# Importing necessary packages

# <codecell>

#!pip install nltk

# <codecell>

import os
import pandas as pd
from IIPE.preproc import make_contents_df, make_tokens
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation

# <markdowncell>

# Select the data_samples to read .txt files

# <codecell>

print(os.getcwd())
os.chdir(os.path.join('..', 'IIPE', 'data_sample', 'plain_text_sample'))
print(os.getcwd())

# <codecell>

file_names = os.listdir()
file_names

# <markdowncell>

# ## Use our preprocessing functions

# <codecell>

df_contents = make_contents_df(file_names)
df_contents

# <codecell>

tokens = make_tokens(df_contents)
print(len(tokens), ' tokens available. Here are the 5 first in no particular order: ')
tokens[:5]

# <codecell>

from IIPE.constants import ALL_STOP_WORDS
from sklearn.feature_extraction import text

# <codecell>

all_stop_words = text.ENGLISH_STOP_WORDS.union(ALL_STOP_WORDS)
type(all_stop_words), len(all_stop_words)

# <codecell>

vectorizer = TfidfVectorizer().fit(df_contents['text'])

data_vectorized = vectorizer.transform(df_contents['text'])

lda_model = LatentDirichletAllocation(n_components=2).fit(data_vectorized)

def print_topics(model, vectorizer):
    for idx, topic in enumerate(model.components_):
        print("Topic %d:" % (idx))
        print([(vectorizer.get_feature_names()[i], topic[i])
                        for i in topic.argsort()[:-10 - 1:-1]])
        

print_topics(lda_model, vectorizer)

# <codecell>

vectorizer = TfidfVectorizer(stop_words=all_stop_words).fit(df_contents['text'])

data_vectorized = vectorizer.transform(df_contents['text'])

lda_model = LatentDirichletAllocation(n_components=2).fit(data_vectorized)

def print_topics(model, vectorizer):
    for idx, topic in enumerate(model.components_):
        print("Topic %d:" % (idx))
        print([(vectorizer.get_feature_names()[i], topic[i])
                        for i in topic.argsort()[:-10 - 1:-1]])
        

print_topics(lda_model, vectorizer)


# <markdowncell>

# ## Topic modelling

# <codecell>


