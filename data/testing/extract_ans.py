# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 17:04:01 2021

@author: Akhil
"""
import nltk
nltk.download('punkt')
from pipelines import answer_pipeline
from nltk import sent_tokenize
import pickle
x=answer_pipeline("answer-extraction",ans_model="valhalla/t5-small-qa-qg-hl",ans_tokenizer="valhalla/t5-small-qa-qg-hl")
f=open("context.pkl","rb")
context=pickle.load(f)
d=dict()
gen_ans=[]
for l in context:
    pres_ans=[]
    for i in x(l):
        sent=i[0]
        ans=i[1]
        if sent not in d:
            d[sent]=[]
        for a in ans:
            new_a=(a.strip("<pad>")).strip()
            if new_a not in d[sent]:
                d[sent].append(new_a)
                pres_ans.append(new_a)
    for i in sent_tokenize(l):
        if i not in d:
            d[i]=[]
        for j in x(i):
            for ans in j[1]:
                a=(ans.strip("<pad>")).strip()
                if a not in d[i]:
                    d[i].append(a)
                    pres_ans.append(a)
    gen_ans.append(pres_ans)
f.close()
with open('gen_ans.pkl','wb') as f:
    pickle.dump(gen_ans,f)
f.close()
with open('gen_ans_dict.pkl','wb') as f:
    pickle.dump(d,f)
f.close()