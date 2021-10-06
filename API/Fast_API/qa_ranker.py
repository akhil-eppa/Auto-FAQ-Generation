def generate_qa_pairs(qa_dict):
	QAs=[]
	for qa in qa_dict:
		for question in enumerate(qa['questions']):
			pair={}
			pair['sentence']=qa['sentence']
			pair['question']=question[1]
			pair['answer']=qa['answers'][question[0]]["answer"]
			pair['score']=qa['answers'][question[0]]["score"]
			QAs.append(pair)
	QAs.sort(key=lambda x:x["score"],reverse=True)
	return QAs