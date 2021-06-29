# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 16:40:56 2021

@author: Akhil
"""

from rouge import Rouge
import pickle
f=open("actual_gold_ans.pkl","rb")
ref_ans=pickle.load(f)
f.close()
f=open("spanbert_gold_ans.pkl","rb")
gen_ans=pickle.load(f)
f.close()
'''
for i in range(len(ref_ans)):
    ref=[]
    t=(ref_ans[i].lower()).split(' ')
    ref.append(t)
    #print(ref)
    gen=(gen_ans[i].lower()).split(' ')
    #print(gen)
'''
rouge=Rouge()
print(rouge.get_scores(gen_ans, ref_ans, avg=True))

'''
{'rouge-1': {'f': 0.8369990664386885, 'p': 0.878018846676446, 'r': 0.8490035587075188}, 
 'rouge-2': {'f': 0.5088053329148368, 'p': 0.5339490575867574, 'r': 0.517632302513214}, 
 'rouge-l': {'f': 0.8384242551860608, 'p': 0.8785660224178982, 'r': 0.8499948161992177}}
'''