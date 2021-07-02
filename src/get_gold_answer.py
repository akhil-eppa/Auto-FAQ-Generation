# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 10:25:30 2021

@author: Akhil
"""

from transformers import pipeline

qa_pipeline = pipeline(
    "question-answering",
    model="mrm8488/spanbert-finetuned-squadv1",
    tokenizer="mrm8488/spanbert-finetuned-squadv1"
)

def extract_gold_ans(context,question):
    response = qa_pipeline({'context': context,'question': question})
    return response