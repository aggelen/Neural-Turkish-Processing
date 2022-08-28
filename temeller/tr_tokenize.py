#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 19:32:48 2022

@author: aggelen
"""
import nltk
nltk.download('tagsets')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

from nltk.tokenize import word_tokenize


t1 = "Bir gün bu akan sele dur diyeceğim, göreceksin. Ne bu şehir kalacak, ne bu duygusuz sürü, "
t2 = "bu korkunç kalabalık. Her vapur seni getirecek bana. Bütün istasyonlarda seni bekleyeceğim. "
t3 = "Kapılar sana açılacak. Senin için söylenecek şarkılar. Şiirler senin için yazılacak. "
t4 = "Her evde bir resmin, her meydanda bir heykelin olacak. Ve sen kimi gün bir rüzgar gibi, "
t5 = "kimi gün denizler gibi, bulutlar gibi, kopup ötelerden, ötelerden, yalnız bana geleceksin. "
t6 = "Bir gün bu akan sele dur diyeceğim göreceksin."
t = t1 + t2 + t3 + t4 + t5 + t6

tokenized = word_tokenize(t)

tags = nltk.pos_tag(tokenized)