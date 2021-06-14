# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 11:15:16 2021

@author: Akhil
"""

import nltk
nltk.download('punkt')
from pipelines import answer_pipeline
x=answer_pipeline("answer-extraction",ans_model="valhalla/t5-small-qa-qg-hl",ans_tokenizer="valhalla/t5-small-qa-qg-hl")
print(x("George Lucas directed Star Wars."))