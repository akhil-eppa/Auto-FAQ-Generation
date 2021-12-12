from advertools import knowledge_graph
import pandas as pd
import spacy
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from get_answer_v2 import extract_answers
from question_generator import get_questions
from get_gold_answer import get_gold_answer
from qa_ranker import generate_qa_pairs


nlp=spacy.load("en_core_web_sm")

def get_Entities(context):
  doc=nlp(context)
  ner=[]
  for ent in doc.ents:
    entity={}
    entity['text']=ent.text
    entity['label']=ent.label_
    entity['pos_start']=ent.start_char
    entity['pos_end']=ent.end_char
    ner.append(entity)
  return ner

def get_questions_definition(context):
    entities=get_Entities(context)
    questions=[]
    key="AIzaSyC_kVxenahbYF-Y4-YKIhrjVgvEUGgtvNw"
    for entity in entities:
        if entity["label"] == "ORG" or entity["label"]=="PERSON" or entity["label"] == "LOC" or entity["label"] == "GPE":
            kg_df = knowledge_graph(key=key, query=entity["text"],types=entity["label"])
            kg_df = kg_df.fillna('')
            question={}
            df=kg_df[['result.name','result.description', 'resultScore','result.detailedDescription.articleBody']]
            if entity["label"] == "ORG":
              question["ques"]="What is " + entity["text"] + "?"
            if entity["label"] == "PERSON":
              question["ques"]="Who is " + entity["text"] + "?"
            if entity["label"] == "LOC" or entity["label"] == "GPE":
              question["ques"]="Where is " + entity["text"] + "?"
            try:
              question["ans"]=df.iloc[0,3]
              questions.append(question)
            except ValueError:
              continue
            except Exception as e:
              continue
    return questions
  
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
async def home():
  return {'message': "Welcome to FAQ Generator API!"}


@app.get('/extra')
async def generate_extra_questions(context : str):
  extras = get_questions_definition(context)
  
  return extras

@app.get('/api')
async def generate_faqs(context : str, limit : int = 20):
  print(context, limit)
  qa_dict = extract_answers(context)
  get_questions(qa_dict)
  get_gold_answer(qa_dict)
  FAQs = generate_qa_pairs(qa_dict, limit)

  return FAQs
  
@app.post('/test')
async def test():
  return [
    {
        "sentence": "Star Wars was released in 1979.",
        "question": "What movie was released in 1979?",
        "answer": "Star Wars",
        "score": 0.9977646470069885
    },
    {
        "sentence": "Star Wars was released in 1979.",
        "question": "When was Star Wars released?",
        "answer": "1979",
        "score": 0.9922865629196167
    },
    {
        "sentence": "It was directed by George Lucas.",
        "question": "Who directed the film?",
        "answer": "George Lucas",
        "score": 0.9744633436203003
    }
]
