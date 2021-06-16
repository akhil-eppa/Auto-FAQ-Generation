# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 11:09:01 2021

@author: Akhil
"""
import pickle
f=open("ref_ans.pkl","rb")
ref_ans=pickle.load(f)
f.close()
f=open("gen_ans_updated.pkl","rb")
gen_ans=pickle.load(f)
f.close()
from nltk.translate.bleu_score import corpus_bleu
ans=0
count=0
'''
for i in ref_ans:
    for j in i:
        for k in j:
            k=k.lower()
'''
for i in range(len(ref_ans)):
    ref=ref_ans[i]
    reference=[]
    reference.append(ref)
    gen=list(set(gen_ans[i]))

    for j in gen:
        candidate=[]
        candidate.append(j.split())
        ans+=corpus_bleu(reference,candidate,weights=(1,0,0,0))
        count+=1
print("Individual 1 gram=",ans/count)
ans=0
count=0
for i in range(len(ref_ans)):
    ref=ref_ans[i]
    reference=[]
    reference.append(ref)
    gen=list(set(gen_ans[i]))

    for j in gen:
        candidate=[]
        candidate.append(j.split())
        ans+=corpus_bleu(reference,candidate,weights=(0,1,0,0))
        count+=1
print("Individual 2 gram=",ans/count)
ans=0
count=0
for i in range(len(ref_ans)):
    ref=ref_ans[i]
    reference=[]
    reference.append(ref)
    gen=list(set(gen_ans[i]))

    for j in gen:
        candidate=[]
        candidate.append(j.split())
        ans+=corpus_bleu(reference,candidate,weights=(0.5,0.5,0,0))
        count+=1
print("Cumulative 2 gram=",ans/count)
'''
Individual 1 gram= 0.3480729458914097
Individual 2 gram= 0.18173964196093523
Cumulative 2 gram= 0.18551717313193114
'''

'''
Adding more answers through identifying noun phrases
Individual 1 gram= 0.189024243406113
Individual 2 gram= 0.10318939398505136
Cumulative 2 gram= 0.10504336038658749
'''