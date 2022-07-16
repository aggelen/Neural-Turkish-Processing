#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 14:36:33 2022

@author: aggelen
"""

import nltk
import spacy

nltk.download('stopwords')

#%%
from nltk.corpus import stopwords
stop_words = stopwords.words('english')

#%%
nlp = spacy.load('en_core_web_sm')