# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 10:25:30 2021

@author: Akhil
"""

from transformers import pipeline



def get_gold_answer(qa_dict):
    for qa in qa_dict:
        for question in qa['questions']:
            qa['answers'].append(extract_gold_ans(qa['sentence'],question))

def extract_gold_ans(context,question):
    qa_pipeline = pipeline(
    "question-answering",
    model="mrm8488/spanbert-finetuned-squadv1",
    tokenizer="mrm8488/spanbert-finetuned-squadv1"
)
    response = qa_pipeline({'context': context,'question': question})
    return response