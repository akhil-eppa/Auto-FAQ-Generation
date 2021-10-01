# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 13:20:31 2021

@author: Akhil
"""

import tensorflow_hub as hub
from sklearn.metrics.pairwise import cosine_similarity
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch
from nltk import sent_tokenize
# nltk.download('punkt')
USE_url="https://tfhub.dev/google/universal-sentence-encoder/4"
embed = hub.load(USE_url)
#from transformers import pipeline
#summarizer = pipeline("summarization")
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
      #, no_repeat_ngram_size=2
      summary_ids = model.generate(tokenized_text, num_beams=4, length_penalty=-1.0, min_length=10, max_length=50, temperature=0.7, early_stopping=True)
      output = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
      summs.append(output)
    return summs

def get_coherent_sentences(x):
    m=get_coherence_matrix(x)
    c=get_sentence_combination(x, m)
    summs=get_summaries(c)
    return summs

if __name__=="__main__":
    x=["This is a test to check how combinations are extracted.","These combinations are used for summarizations.","Answers are extracted from summarizations.","Later these are used for final question answer generation."]
    '''
    print("Matrix Generation Started")
    m=get_coherence_matrix(x)
    print("Matrix Generated.")
    print(m)
    print("Getting Sentence Combinations")
    c=get_sentence_combination(x, m)
    print(c)
    print("Summarization_Started.")
    summs=get_summaries(c)
    print(summs)
    '''
    x='''Star Wars is an American epic space opera[1] media franchise created by George Lucas, which began with the eponymous 1977 film[b] and quickly became a worldwide pop-culture phenomenon. The franchise has been expanded into various films and other media, including television series, video games, novels, comic books, theme park attractions, and themed areas, comprising an all-encompassing fictional universe.[c] In 2020, its total value was estimated at US$70 billion, and it is currently the fifth-highest-grossing media franchise of all time.
    The original film (Star Wars), retroactively subtitled Episode IV: A New Hope (1977), was followed by the sequels Episode V: The Empire Strikes Back (1980) and Episode VI: Return of the Jedi (1983), forming the original Star Wars trilogy. Lucas later returned to filmmaking to direct a prequel trilogy, consisting of Episode I: The Phantom Menace (1999), Episode II: Attack of the Clones (2002), and Episode III: Revenge of the Sith (2005). In 2012, Lucas sold his production company to Disney, relinquishing his ownership of the franchise. The subsequently produced sequel trilogy consists of Episode VII: The Force Awakens (2015), Episode VIII: The Last Jedi (2017), and Episode IX: The Rise of Skywalker (2019).
    '''
    x=sent_tokenize(x)
    print(get_coherent_sentences(x))
        