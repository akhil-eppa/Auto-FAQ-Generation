# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 13:20:31 2021
@author: Akhil
"""

import tensorflow_hub as hub
from sklearn.metrics.pairwise import cosine_similarity
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

USE_url="https://tfhub.dev/google/universal-sentence-encoder/4"
embed = hub.load(USE_url)
model = T5ForConditionalGeneration.from_pretrained('t5-small')
tokenizer = T5Tokenizer.from_pretrained('t5-small')
device = torch.device('cpu')

def get_coherence_matrix(sents):
    x=[[0 for i in range(len(sents))] for i in range(len(sents))]
    v=[]
    for i in sents:
        v.append(embed([i]))
    for i in range(len(sents)):
        for j in range(i,len(sents)):
            if i==j:
                x[i][j]=1
            else:
                c=cosine_similarity(v[i],v[j])
                x[i][j]=c
                x[j][i]=c
    return x

def get_sentence_combination(sents,matrix):
    combs=[]
    for i in range(1,len(matrix)-1):
        before=""
        after=""
        m=float("-inf")
        m_ind=-1
        for b in range(0,i):
            if matrix[i][b]>m:
                m=matrix[i][b]
                m_ind=b
        before=sents[m_ind]
        m=float("-inf")
        m_ind=-1
        for a in range(i+1,len(matrix)):
            if matrix[i][a]>m:
                m=matrix[i][a]
                m_ind=a
        after=sents[m_ind]
        ans=before+sents[i]+after
        combs.append(ans)
    return combs

def get_summaries(combinations):
    summs=[]
    for i in combinations:
      preprocess_text = i.strip().replace("\n","")
      t5_prepared_Text = "summarize: "+preprocess_text
      tokenized_text = tokenizer.encode(t5_prepared_Text, return_tensors="pt").to(device)
      summary_ids = model.generate(tokenized_text, num_beams=4, length_penalty=-1.0, min_length=10, max_length=50, temperature=0.7, early_stopping=True)
      output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
      summs.append(output)
    return summs

def get_coherent_sentences(x):
    m=get_coherence_matrix(x)
    c=get_sentence_combination(x, m)
    summs=get_summaries(c)
    return summs