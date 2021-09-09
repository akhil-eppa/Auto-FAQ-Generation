# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 18:27:35 2021

@author: Akhil
"""

from get_answer_v2 import extract_answers
from get_gold_answer_v2 import extract_gold_ans
def get_qas(passage):
    '''
    generates list of dictionaries
    '''
    qa_dict=extract_answers(passage)
    
    '''
    TO BE ADDED 
    Steps to be executed to generate questions
    
    for item in qa_dict:
        sent=item["sentence"]
        for sp in item["spans"]:
            q=get_question(sent,sp)
            item["questions"].append(q)
    '''
    
    for item in qa_dict:
        sent=item["sentence"]
        for q in item["questions"]:
            res,extra=extract_gold_ans(sent,q)
            if extra!=None:
                res["answer"]=res["answer"]+".\nAdditional Information for Context:"+extra
            item["answers"].append(res)
    
    