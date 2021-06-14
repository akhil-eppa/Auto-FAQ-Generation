# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 11:15:16 2021

@author: Akhil
"""

import nltk
nltk.download('punkt')
from pipelines import answer_pipeline
x=answer_pipeline("answer-extraction",ans_model="valhalla/t5-small-qa-qg-hl",ans_tokenizer="valhalla/t5-small-qa-qg-hl")
l="Architecturally, the school has a Catholic character. \
Atop the Main Building's gold dome is a golden statue of the Virgin Mary.\
Immediately in front of the Main Building and facing it, is a copper statue of Christ with arms upraised with the legend \"Venite Ad Me Omnes\". Next to the Main Building is the Basilica of the Sacred Heart. Immediately behind the basilica is the Grotto, a Marian place of prayer and reflection. It is a replica of the grotto at Lourdes, France where the Virgin Mary reputedly appeared to Saint Bernadette Soubirous in 1858. At the end of the main drive (and in a direct line that connects through 3 statues and the Gold Dome), is a simple, modern stone statue of Mary."

print(x(l))
for i in nltk.sent_tokenize(l):
    print(x(i))