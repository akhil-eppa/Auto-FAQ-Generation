# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 15:28:26 2021

@author: Akhil
"""

import nltk
nltk.download('punkt')
from pipelines import answer_pipeline
from nltk import sent_tokenize
nltk.download('averaged_perceptron_tagger')
import nltk.tokenize as nt
import pickle
from textblob import TextBlob
'''
python -m textblob.download_corpora
'''
def get_entities(sent):
    ans=[]
    b=TextBlob(sent)
    for n in b.noun_phrases:
        if len(n)>4 and n not in ans:
            if n[0] not in ["'"]:
                ans.append(n)
    return ans
x=answer_pipeline("answer-extraction",ans_model="valhalla/t5-small-qa-qg-hl",ans_tokenizer="valhalla/t5-small-qa-qg-hl")
f=open("context.pkl","rb")
context=pickle.load(f)
d=dict()
gen_ans=[]
for l in context[:1]:
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
    gen_ans.append(pres_ans)
f.close()
with open('gen_ans.pkl','wb') as f:
    pickle.dump(gen_ans,f)
f.close()
with open('gen_ans_dict.pkl','wb') as f:
    pickle.dump(d,f)
f.close()