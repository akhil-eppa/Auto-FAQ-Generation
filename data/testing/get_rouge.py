# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 10:55:29 2021

@author: Akhil
"""

from rouge import Rouge
import pickle
f=open("ref_ans.pkl","rb")
ref_ans=pickle.load(f)
f.close()
f=open("gen_ans_updated.pkl","rb")#change to gen_ans.pkl to test for without noun phrases extractions
gen_ans=pickle.load(f)
f.close()
ref=[]
for i in ref_ans:
    temp=[]
    for j in i:
        if "\"" in j:
            j.remove("\"")
        x=" ".join(j)
        x=x.lower()
        x=''.join(e for e in x if e.isalnum() or e==" ")
        temp.append(x)
    ref.append(" ".join(temp))
gen=[]
for i in gen_ans:
    x=" ".join(i)
    x=x.lower()
    x=''.join(e for e in x if e.isalnum() or e==" ")
    gen.append(x)

rouge=Rouge()
print(rouge.get_scores(gen, ref, avg=True))

'''
Without Noun Phrases Extraction
{'rouge-1': {'f': 0.3711157619132118, 'p': 0.3427736975943852, 'r': 0.5426197787867881},
'rouge-2': {'f': 0.1988688392097367, 'p': 0.18777538386850504, 'r': 0.29121825872689966},
'rouge-l': {'f': 0.3403931622201618, 'p': 0.320271298645147, 'r': 0.45803814028554596}}


With Noun Phrases Extraction
{'rouge-1': {'f': 0.3168794193101276, 'p': 0.22684031589564888, 'r': 0.7205923874645691},
'rouge-2': {'f': 0.15986328911488842, 'p': 0.1145638866388487, 'r': 0.36813752655213844},
'rouge-l': {'f': 0.3187056609390848, 'p': 0.23673021814492376, 'r': 0.6169324652448179}}
'''
#print(ref[0])
#print(gen[0])
#print(gen_ans[0])