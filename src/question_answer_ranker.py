from transformers import pipeline
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
    sorted_list = sorted(list_of_dictionaries, key=lambda k: k["score"], reverse=True) #Score key is appended when pre-trained model assigns value
    return sorted_list

'''
Given list of dictionaries with sentence(context),span,question and answer, it focuses only on QA and using a pre-trained model scores them and also appends
the score as one of the keys of the dictionary
'''
def rank_qa_pairs(list_of_dictionaries):
    for i in list_of_dictionaries:
        rank_score = qapair_rank_pipeline(i["questions"], i["answers"])
        i["score"] = rank_score["Score"]
    sort_list(list_of_dictionaries)