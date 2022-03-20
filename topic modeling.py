# -*- coding: utf-8 -*-
"""
Created on Fri Mar 18 11:54:52 2022

@author: LEVEL51PC
"""
import pandas as pd


#Gensim
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel
#spacy
import spacy

from nltk.corpus import stopwords
#vis
import pyLDAvis
import pyLDAvis.gensim_models as gensimvis
stopwords = stopwords.words('english')

df = pd.read_csv('C:/Users/LEVEL51PC/Desktop/Essex/Frontrunner/premierleague/cleaned_data.csv',index_col=0)
df.dropna(inplace=True)
titles = df['title'].tolist()

def lemmatization(texts, allowed_postags=["NOUN", "ADJ", "VERB", "ADV"]):
    nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])
    texts_out = []
    for text in texts:
        doc = nlp(text)
        new_text = []
        for token in doc:
            if token.pos_ in allowed_postags:
                new_text.append(token.lemma_)
        final = " ".join(new_text)
        texts_out.append(final)
    return (texts_out)


def gen_words(texts):
    final = []
    for text in texts:
        new = gensim.utils.simple_preprocess(text, deacc=True)
        final.append(new)
    return (final)

lemmatized_titles = lemmatization(titles)

data_words = gen_words(lemmatized_titles)

id2word = corpora.Dictionary(data_words)

corpus = []
for text in data_words:
    new = id2word.doc2bow(text)
    corpus.append(new)


lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus,
                                           id2word=id2word,
                                           num_topics=20,
                                           random_state=100,
                                           update_every=1,
                                           chunksize=100,
                                           passes=10,
                                           alpha="auto")

pyLDAvis.enable_notebook()
vis = gensimvis.prepare(lda_model, corpus, id2word, mds="mmds", R=20)
vis

