# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 17:43:58 2021

@author: Akhil
"""

import json
f=open(r"dev-v1.1.json")
d=json.load(f)
from nltk import sent_tokenize
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




result=[]
context=[]
ref_ans=[]
for sub in d["data"]:
    for para in sub["paragraphs"]:
        context.append(para["context"])
        cont=para["context"]
        sents=sent_tokenize(cont)
        ind=dict()
        for i in sents:
            start=cont.find(i)
            end=start+len(i)
            ind[(start,end)]=i
        #ans=[]
        for i in para["qas"]:
            ans=i["answers"][0]["text"]
            starting=i["answers"][0]["answer_start"]
            ques=i["question"]
            for index in ind:
                if starting>=index[0] and starting<index[1]:
                    sent=ind[index]
            total=dict()
            total["context"]=cont
            total["sentence"]=sent
            total["question"]=ques
            total["answer"]=ans
            if total not in ref_ans:
                ref_ans.append(total)
import pickle
with open('squad_formatted.pkl','wb') as f:
    pickle.dump(ref_ans,f)
f.close()
'''
import pickle
with open('context.pkl','wb') as f:
    pickle.dump(context,f)
f.close()
with open('ref_ans.pkl','wb') as f:
    pickle.dump(ref_ans,f)
f.close()
'''



import re
  
# initializing string
test_str = 'Star Wars was directed by George Lucas. George Lucas directed many trilogies.'
sents=sent_tokenize(test_str)
for i in sents:
    start=test_str.find(i)
    end=start+len(i)
    print(test_str.find(i))
    print(test_str[start:end])
# printing original string
#print("The original string is : " + str(test_str))
  
# regex to get words, loop to get each start and end index
#res = [(ele.start(), ele.end() - 1) for ele in sents]
  
# printing result
#print("Word Ranges are : " + str(res))