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
def rank_qa_pairs():
    # Can write code only when model is found and finalised 