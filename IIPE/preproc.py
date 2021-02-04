import os
import pandas as pd
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from IIPE.constants import NEW_STOP_WORDS

"""
Module to create tokens out of the extracted text in module scrape.py
Used, fixed and adapted some code from https://github.com/iiepdev/Inspection_Reports/blob/main/Ireland_Analysis.ipynb
"""


def make_contents_df(lst):
    """Returns a dataframe with date, reference, text from a list of file_names"""
    # init a list of dictionnaries
    ld_contents = []

    for file in lst:
        if file.endswith(".txt"):
            # keeping the reference and the date
            split = (
                file.replace("Reports_Plain text_", "").replace(".txt", "").split("_")
            )
            reference = split[0]
            date = "-".join(split[1:][::-1])

            # creating the dictionnary
            d = {"date": date, "reference": reference, "text": ""}

            # adding text content to the dictionary
            with open(file, encoding="utf8", errors="ignore") as f:
                text = f.read()
                d["text"] = text
            ld_contents.append(d)

    # create dataframe and set date to a datetime datatype
    df_contents = pd.DataFrame(ld_contents)
    df_contents["date"] = pd.to_datetime(df_contents["date"])
    return df_contents


def make_tokens(df):
    """Removes stopwords, stems and lemmatizes.  Returns clean tokens."""

    stopwords = set(nltk.corpus.stopwords.words("english"))

    # turns the text in the dataframe into a long list of words
    TotalText = list(df.text.values)

    # stopwords, with plurals (otherwise the lemmatizong steps puts some of the stopwords back)
    NEW_STOP_WORDS
    stopwords = stopwords.union(NEW_STOP_WORDS)
    TotalText = " ".join(TotalText)

    # tokenization
    tokens = [
        w for w in word_tokenize(TotalText.lower()) if w.isalpha()
    ]  # isalpha() checks if each word is alphabetical, lower() transforms everything to lowercase
    no_stop = [
        t.strip() for t in tokens if t.strip() not in stopwords
    ]  # stopwords already comes with a built-in list of words to remove
    wordnet_lemmatizer = WordNetLemmatizer()
    lemmatized = [wordnet_lemmatizer.lemmatize(t) for t in no_stop]

    return lemmatized


if __name__ == "__main__":
    os.chdir(os.path.join("data_sample", "plain_text_sample"))
    # print(os.getcwd())
    # print("Files to be processed : ", os.listdir())

    df = make_contents_df(os.listdir())
    # print(df)
    tokens = make_tokens(df)
    # print(tokens)

    # TO DO : convert the prints below into unit tests
    # print(df.shape)
    # print(df.dtypes)
    print(f"We have {len(tokens)} tokens")
