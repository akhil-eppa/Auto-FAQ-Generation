# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 12:32:10 2021
@author: Akhil
"""

import nltk
nltk.download('punkt')
nltk.download('brown')
nltk.download('averaged_perceptron_tagger')

from nltk import sent_tokenize
from textblob import TextBlob

from pipelines import answer_pipeline
from coherence_span import get_coherent_sentences

def get_entities(sent):
    ans=[]
    b=TextBlob(sent)
    for n in b.noun_phrases:
        if len(n)>4 and n not in ans:
            if n[0] not in ["'"]:
                ans.append(n)
    return ans
x=answer_pipeline("answer-extraction",ans_model="valhalla/t5-small-qa-qg-hl",ans_tokenizer="valhalla/t5-small-qa-qg-hl")


'''
Given a passage of text this function will return a list of dictionaries.
Each dictionary has the following keys:
    'sentence' -> Holds an individual sentence from passage
    'spans' -> list of spans extarcted from the given passage
    'questions' -> an empty list initialized. Will be filled with questions from question generation module
    'answers' -> an empty list initialized. Will be filled with answers from answer generation module
'''
def extract_answers(context):
    pres_ans=[]
    gen_ans=[]
    c=sent_tokenize(context)
    d=dict()
    for i in x(context):
        pres_ans=[]
        sent=i[0]
        ans=i[1]
        if sent not in d:
            d[sent]=[]
        for a in ans:
            new_a=(a.strip("<pad>")).strip()
            if new_a not in d[sent]:
                d[sent].append(new_a)
                pres_ans.append(new_a)
        for j in x(sent):
            for ans in j[1]:
                a=(ans.strip("<pad>")).strip()
                if a not in d[sent]:
                    d[sent].append(a)
                    pres_ans.append(a)
        ent=get_entities(sent)
        temp_pres_ans=[i.lower() for i in pres_ans]
        for n in ent:
            if n not in temp_pres_ans:
                temp_pres_ans.append(n)
                pres_ans.append(n)
                d[sent].append(n)
    combs=get_coherent_sentences(c)
    for i in combs:
        for j in x(i):
            pres_ans=[]
            sent=j[0]
            ans=j[1]
            if sent not in d:
                d[sent]=[]
            for a in ans:
                new_a=(a.strip("<pad>")).strip()
                if new_a not in d[sent] and abs(len(new_a)-len(sent))>5:
                    d[sent].append(new_a)
                    pres_ans.append(new_a)
            ent=get_entities(sent)
            temp_pres_ans=[i.lower() for i in pres_ans]
            for n in ent:
                if n not in temp_pres_ans:
                    temp_pres_ans.append(n)
                    pres_ans.append(n)
                    d[sent].append(n)
    ind_answer={}
    for i in d:
        ind_answer={}
        ind_answer["sentence"]=i
        ind_answer["spans"]=d[i]
        ind_answer["questions"]=[]
        ind_answer["answers"]=[]
        gen_ans.append(ind_answer)
    return gen_ans
