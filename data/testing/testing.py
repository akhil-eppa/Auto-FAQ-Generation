# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 15:32:16 2021

@author: Akhil
"""

import json
f=open(r"dev-v1.1.json")
d=json.load(f)

'''
print(len(d["data"]))
print(len(d["data"][0]['paragraphs'][0]["qas"]))
#print(d["data"][0]['paragraphs'][0]["context"])
for i in d["data"][0]["paragraphs"][0]["qas"]:
    print("Q:", i["question"])
    print("A:", i["answers"][0]["text"])
    
'''    
'''
json data
d["data"] -> list of passages and question answers related to different topics
data[0] -> title
data[0] -> paragraphs
d["data"][0]["paragraphs"]
d["data"][0]["paragraphs"][0]["context"]
d["data"][0]["paragraphs"][0]["qas"]

'''
context=[]
ref_ans=[]
for sub in d["data"]:
    for para in sub["paragraphs"]:
        context.append(para["context"])
        ans=[]
        for i in para["qas"]:
            x=i["answers"][0]["text"].split()
            if x not in ans:
                ans.append(x)
        ref_ans.append(ans)
import pickle
with open('context.pkl','wb') as f:
    pickle.dump(context,f)
f.close()
with open('ref_ans.pkl','wb') as f:
    pickle.dump(ref_ans,f)
f.close()
'''
for i in range(len(ref_ans)):
    print(context[i])
    print(ref_ans[i])
    print("****************************\n")
'''