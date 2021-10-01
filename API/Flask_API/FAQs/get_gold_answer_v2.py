# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 10:25:30 2021

@author: Akhil
"""
from textblob import TextBlob
from advertools import knowledge_graph
key="AIzaSyC_kVxenahbYF-Y4-YKIhrjVgvEUGgtvNw"
from transformers import pipeline

qa_pipeline = pipeline(
    "question-answering",
    model="mrm8488/spanbert-finetuned-squadv1",
    tokenizer="mrm8488/spanbert-finetuned-squadv1"
)

def is_proper_entity(text):
    words=text.split(" ")
    res=TextBlob(text)
    l=len(words)
    count_p=0
    count_c=0
    for i in res.tags:
        if i[1]=='NNP':
            count_p+=1
        elif i[1]=='NN' or i[1]=='NNS':
            count_c+=1
    if l==count_p:
        return True
    if l==count_c:
        asc=[ord(i[0]) for i in words]
        asc=[i for i in asc if i>=65 and i<=90]
        if len(asc)==l:
            return True
        else:
            return False
    return False

def get_additional_details(answer):
    if is_proper_entity(answer):
        try:
            kg_details=knowledge_graph(key=key, query=answer)
            return kg_details["result.detailedDescription.articleBody"][0]
        except:
            return None
    else:
        return None

def extract_gold_ans(context,question):
    response = qa_pipeline({'context': context,'question': question})
    extra=get_additional_details(response["answer"])
    return response,extra

if __name__=="__main__":
    response,extra=extract_gold_ans("Star Wars released in 1977.","What released in 1977?")
    print(response,extra)