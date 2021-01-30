# -*- coding: utf-8 -*-
# <nbformat>4</nbformat>

# <markdowncell>

# # Preprocessing from package

# <markdowncell>

# ## Imports packages and sample .txt

# <markdowncell>

# Checking virtualenv with `pyenv`

# <codecell>

#!pyenv virtualenvs

# <markdowncell>

# Importing necessary packages

# <codecell>

#!pip install nltk

# <codecell>

import os
import pandas as pd
import matplotlib.pyplot as plt
import nltk, re
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from collections import Counter

# <markdowncell>

# Select the data_samples to read .txt files

# <codecell>

#run only once, multiple runs will give an error =>restart kernel
print(os.getcwd())
os.chdir(os.path.join('..', 'IIPE', 'data_sample', 'plain_text_sample'))
os.getcwd()

# <codecell>

file_names = os.listdir()
file_names

# <markdowncell>

# ## Clean file names

# <markdowncell>

# Clean file names, return ref and date YYYY-MM-DD format

# <codecell>

def clean_file_names(lst):
    """returns a list of tuples<reference, date>"""
    cleaned = [name.replace('Reports_Plain text_','').replace('.txt','') for name in os.listdir()]
    splitted = [name.split('_') for name in cleaned]
    references = [lst[0] for lst in splitted]
    dates = ['-'.join(name[1:][::-1]) for name in splitted]
    return [(r,d) for r, d in zip(references, dates)]


# <codecell>

clean_file_names(os.listdir())

# <markdowncell>

# ## Cleaning unusefull content

# <markdowncell>

# Read `.txt`files into a pandas.Dataframe

# <codecell>

def make_contents_df(lst):
    """Returns a dataframe with date, reference, text from a list of file_names"""
    #init a list of dictionnaries
    ld_contents = []
    
    for file in file_names:
        # keeping the reference and the date
        split = file.replace('Reports_Plain text_','').replace('.txt','').split('_')
        reference = split[0]
        date= '-'.join(split[1:][::-1])

        #creating the dictionnary
        d = {'date':date,
             'reference':reference,
             'text': '' }

        #adding text content to the dictionary
        with open(file) as f:
            text = f.read()
            d['text']=text
        ld_contents.append(d)
    #create dataframe and set date to a datetime datatype

    df_contents = pd.DataFrame(ld_contents)
    df_contents['date'] = pd.to_datetime(df_contents['date'])
    return df_contents

# <codecell>

df_FilesProperlyConverted = make_contents_df(file_names)
df_FilesProperlyConverted

# <markdowncell>

# ### Most used words


# <codecell>

stopwords = set(nltk.corpus.stopwords.words('english'))

TotalText = []
for index, row in df_FilesProperlyConverted.iterrows():
    text = row['text']
    TotalText.append(text)
newStopWords = ['school','learning','student','pupil','teacher','management','teaching','support', 'lesson', 'board']
newStopWords_plur = ['schools','learnings','students','pupils','teachers','managements','teachings','supports', 'lessons', 'boards']
newStopWords += newStopWords_plur
stopwords = stopwords.union(newStopWords)
TotalText = " ".join(TotalText)
tokens = [w for w in word_tokenize(TotalText.lower()) if w.isalpha()]          # isalpha() checks if each word is alphabetical, lower() transforms everything to lowercase
no_stop = [t.strip() for t in tokens if t.strip() not in stopwords]      # stopwords already comes with a built-in list of words to remove
wordnet_lemmatizer = WordNetLemmatizer()
lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stop]
bow = Counter(lemmatized)
MostCommon = dict(bow.most_common(10))

plt.bar(*zip(*MostCommon.items()))
plt.title('Whole sample')
plt.xlabel('Most common words')
plt.ylabel('Number of times the word appears')
plt.xticks(rotation='vertical')
plt.savefig("Results\\Word count\\Whole sample.png")
plt.show()

# <markdowncell>

# ## Topic modelling

# <codecell>


