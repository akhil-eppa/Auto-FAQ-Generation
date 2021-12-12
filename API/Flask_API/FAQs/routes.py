from flask import request,jsonify
from FAQs import app
from FAQs.get_answer_v2 import extract_answers
from FAQs.question_generator import get_questions
from FAQs.get_gold_answer import get_gold_answer
from FAQs.qa_ranker import generate_qa_pairs

@app.route('/api',methods=['GET','POST'])
def FAQGenerator():
	if request.method=="GET":
		context=request.args['context']
		context=context.replace("\n","")
		print("Extracting answers..")
		qa_dict=extract_answers(context)
		print("Generating Questions..")
		get_questions(qa_dict)
		print("Building FAQs..")
		get_gold_answer(qa_dict)
		QAs=generate_qa_pairs(qa_dict)
		return jsonify(QAs)

