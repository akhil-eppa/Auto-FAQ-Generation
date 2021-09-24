from transformers import pipeline
from get_gold_answer_v2 import extract_gold_ans
# To immediately use a model on a given text, we provide the pipeline API. Pipelines group together a pretrained model with the preprocessing that was used during
# that model's training.
qapair_rank_pipeline = pipeline(
    "question-answering",
    model="iarfmoose/bert-base-cased-qa-evaluator",
    tokenizer="mrm8488/spanbert-finetuned-squadv1"
)

'''
Helper functions that when given a list of dictionaries that contains sentence(context),span,question, answer and score of that particular QA pair, it sorts the 
dictionaries in the descending order of the score (i.e highest score will be first and lowest score will be last)
'''
def sort_list (list_of_dictionaries):
    unsorted_list=list()
    for item in list_of_dictionaries:
        for i in range (len(item["questions"])):
            d=dict()
            d["question"]=item["questions"][i]
            d["answer"]=item["answers"][i]["answer"]
            d["score"]=item["answers"][i]["score"]
            unsorted_list.append(d)
    sorted_list = sorted(unsorted_list, key=lambda k: k["score"], reverse=True)
    if len(sorted_list)<=5:
        return sorted_list
    else:
        filtered_list = [d for d in sorted_list if d["score"]>=0.8]
        return filtered_list

'''
Given list of dictionaries with sentence(context),span,question and answer, it focuses only on QA and using a pre-trained model scores them and also appends
the score as one of the keys of the dictionary
'''
def rank_qa_pairs(list_of_dictionaries):
    for i in list_of_dictionaries:
        rank_score = qapair_rank_pipeline("[CLS]" + i["questions"] + "[SEP]" + i["answers"] + "[SEP]")
        i["score"] = rank_score["LABEL_0"]
    sort_list(list_of_dictionaries)