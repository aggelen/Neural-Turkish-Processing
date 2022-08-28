#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 14:22:23 2022

@author: aggelen
"""
import nltk
from nltk.tokenize import word_tokenize

t = """
Bir gün bu akan sele dur diyeceğim, göreceksin. Ne bu şehir kalacak, ne bu duygusuz sürü,
bu korkunç kalabalık. Her vapur seni getirecek bana. Bütün istasyonlarda seni bekleyeceğim. 
Kapılar sana açılacak. Senin için söylenecek şarkılar. Şiirler senin için yazılacak.
Her evde bir resmin, her meydanda bir heykelin olacak. Ve sen kimi gün bir rüzgar gibi,
kimi gün denizler gibi, bulutlar gibi, kopup ötelerden, ötelerden, yalnız bana geleceksin. 
Bir gün bu akan sele dur diyeceğim göreceksin.
"""

tokens = word_tokenize(t)

#%%
nltk.download("punkt")

def remove_punct(token):
 return [word for word in token if word.isalpha()]

tokens = remove_punct(tokens)

#%% Eng stemming?
# from nltk.stem import PorterStemmer
# ps = PorterStemmer()
# ps_stem_sent = [ps.stem(words_sent) for words_sent in tokens]

from snowballstemmer import TurkishStemmer
turkStem = TurkishStemmer()
stems = [turkStem.stemWord(word) for word in tokens]

#%% Lemm. Eng? (No effect)
nltk.download('wordnet')
nltk.download('omw-1.4')
from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
lem_sent = [lemmatizer.lemmatize(words_sent) for words_sent in tokens]

#%%
import zeyrek
analyzer = zeyrek.MorphAnalyzer()
lem_tokens = [analyzer.lemmatize(words_sent) for words_sent in tokens]