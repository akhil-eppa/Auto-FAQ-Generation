# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 13:22:38 2021

@author: Akhil
"""

import pickle
f=open("actual_gold_ans.pkl","rb")
ref_ans=pickle.load(f)
f.close()
f=open("spanbert_gold_ans.pkl","rb")
gen_ans=pickle.load(f)
f.close()
from nltk.translate.bleu_score import sentence_bleu
one_gram_score=0
two_gram_score=0
cumulative_score=0
count=0
for i in range(len(ref_ans)):
    ref=[]
    t=(ref_ans[i].lower()).split(' ')
    ref.append(t)
    #print(ref)
    gen=(gen_ans[i].lower()).split(' ')
    #print(gen)
    one_gram_score+=sentence_bleu(ref,gen,weights=(1,0))
    two_gram_score+=sentence_bleu(ref,gen,weights=(0,1))
    cumulative_score+=sentence_bleu(ref,gen,weights=(0.5,0.5))
    count+=1
print("Individual 1 gram=",one_gram_score/count)
print("Individual 2 gram=",two_gram_score/count)
print("Cumulative 2 gram=",cumulative_score/count)

'''
Individual 1 gram= 0.7774395706477082
Individual 2 gram= 0.4768997995714859
Cumulative 2 gram= 0.4808301228187186
'''