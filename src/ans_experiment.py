# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 11:15:16 2021

@author: Akhil
"""

import nltk
nltk.download('punkt')
from pipelines import answer_pipeline
from nltk import sent_tokenize
x=answer_pipeline("answer-extraction",ans_model="valhalla/t5-small-qa-qg-hl",ans_tokenizer="valhalla/t5-small-qa-qg-hl")
l="Architecturally, the school has a Catholic character. \
Atop the Main Building's gold dome is a golden statue of the Virgin Mary.\
Immediately in front of the Main Building and facing it, is a copper statue of Christ with arms upraised with the legend \"Venite Ad Me Omnes\". Next to the Main Building is the Basilica of the Sacred Heart. Immediately behind the basilica is the Grotto, a Marian place of prayer and reflection. It is a replica of the grotto at Lourdes, France where the Virgin Mary reputedly appeared to Saint Bernadette Soubirous in 1858. At the end of the main drive (and in a direct line that connects through 3 statues and the Gold Dome), is a simple, modern stone statue of Mary."

'''
keys of d will be sentences and value is a list of answers
'''
d=dict()
'''
First loop is for one-shot approach
The entire paragraph is passed at once.
This generates answers which require a little bit of context
dictionary is maintained to keep track of sentences and answers
extrated from a particular sentence. In this case, the sentence is the key
and the value is a list of answers.
'''
for i in x(l):
    sent=i[0]
    ans=i[1]
    if sent not in d:
        d[sent]=[]
    for a in ans:
        new_a=(a.strip("<pad>")).strip()
        if new_a not in d[sent]:
            d[sent].append(new_a)
            
'''
The second loop below is for a pipelined approach to check for finer answers.
Here the paragraph is split into individual sentences ans passed.
The answers generated here are checked if they already exist. If not,
they are added to the list for a particular sentence. 
'''
for i in sent_tokenize(l):
    if i not in d:
        d[i]=[]
    for j in x(i):
        for ans in j[1]:
            a=(ans.strip("<pad>")).strip()
            if a not in d[i]:
                d[i].append(a)
print(d)