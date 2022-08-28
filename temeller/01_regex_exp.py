#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 14:50:17 2022

@author: aggelen
"""

import re

t = """
Bir gün bu akan sele dur diyeceğim, göreceksin. Ne bu şehir kalacak, ne bu duygusuz sürü,
bu korkunç kalabalık. Her vapur seni getirecek bana. Bütün istasyonlarda seni bekleyeceğim.
22-234-5
Kapılar sana açılacak. Senin için söylenecek şarkılar. Şiirler senin için yazılacak.
Her evde bir resmin, her meydanda bir heykelin olacak. Ve sen kimi gün bir rüzgar gibi,
kimi gün denizler gibi, bulutlar gibi, kopup ötelerden, ötelerden, yalnız bana geleceksin. 
Bir gün bu akan sele dur diyeceğim göreceksin.
"""

#%%
pattern = "meydan"
match = re.search(pattern, t)
res = t[match.span()[0]:match.span()[1]]
res = t[match.start():match.end()]

#%% Multiple
match2 = re.search('seni', t)   #sadece ilk
match_all = re.findall('seni', t)

for m in re.finditer('seni', t):
    print(m.span())    

#%% Spec
pattern = r"(\d{2})-(\d{3})-(\d{1})"
match = re.search(pattern, t)


#%% sub
t2 = """
Bir gün       bu akan sele dur diyeceğim, göreceksin. Ne bu şehir kalacak, ne bu duygusuz sürü,
bu korkunç kalabalık. Her  vapur seni getirecek bana. Bütün istasyonlarda seni bekleyeceğim.
22-234-5
Kapılar sana açılacak. Senin için söylenecek şarkılar. Şiirler senin için yazılacak.
Her evde bir resmin, her meydanda bir heykelin olacak. Ve http://github.com/aggelen/ntp sen kimi gün bir rüzgar gibi,
kimi gün denizler gibi, bulutlar         gibi, kopup ötelerden, ötelerden,           yalnız bana geleceksin. 
Bir gün bu akan sele dur     diyeceğim göreceksin.
"""

clean_txt = re.sub(r"\s+", " ", t2)
urlfree_txt = re.sub(r"http\S+", "", t2)
clean_urlfree_txt = re.sub(r"\s+", " ", re.sub(r"http\S+", "", t2))

rem_pattern = r"(\d{2})-(\d{3})-(\d{1})"
nonumber_txt = re.sub(rem_pattern, "", t2)