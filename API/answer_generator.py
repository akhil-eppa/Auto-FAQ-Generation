from textblob import TextBlob
from advertools import knowledge_graph
from transformers import pipeline

kg_key="AIzaSyC_kVxenahbYF-Y4-YKIhrjVgvEUGgtvNw"

qa_pipeline = pipeline(
    "question-answering",
    model="mrm8488/spanbert-finetuned-squadv1",
    tokenizer="mrm8488/spanbert-finetuned-squadv1"
)

def is_proper_entity(text):
    words=text.split(" ")
    res=TextBlob(text)
    l=len(words)
    count_p=0
    count_c=0
    for i in res.tags:
        if i[1]=='NNP':
            count_p+=1
        elif i[1]=='NN' or i[1]=='NNS':
            count_c+=1
    if l==count_p:
        return True
    if l==count_c:
        asc=[ord(i[0]) for i in words]
        asc=[i for i in asc if i>=65 and i<=90]
        if len(asc)==l:
            return True
        else:
            return False
    return False

def get_additional_details(answer):
    if is_proper_entity(answer):
        try:
            kg_details=knowledge_graph(key=kg_key, query=answer)
            return kg_details["result.detailedDescription.articleBody"][0]
        except:
            return None
    else:
        return None

def get_gold_answer(context, question):
    response = qa_pipeline({'context': context,'question': question})
    extra = get_additional_details(response['answer'])
    result = {
        'answer': response['answer'],
        'score': response['score'],
        'extra': extra
    }
    return result