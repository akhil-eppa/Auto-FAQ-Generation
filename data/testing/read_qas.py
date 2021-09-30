# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 16:42:20 2021

@author: Akhil
"""

import pickle as pkl
with open('squad_formatted.pkl', 'rb') as f:
    data = pkl.load(f)
    #print(data)
    x=dict()
    for i in data:
        if i['context'] not in x:
            x[i['context']]=[]
        t=dict()
        t["question"]=i["question"]
        t["answer"]=i["answer"]
        x[i['context']].append(t)
print(len(x.keys()))
t=list(x.keys())
s=""
for i in range(len(t)):
    s=s+str(t[i])+"\n"
    for j in x[t[i]]:
        s=s+"Question: "+j["question"]+"\n"
        s=s+"Answer: "+j["answer"]+"\n"
    s=s+"\n\n"
file1 = open("SQUAD_QAs.txt","wb")
s=s.encode('utf-8')
file1.write(s)
file1.close()
    