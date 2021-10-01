from flask import request,jsonify
from FAQs import app
from FAQs.get_answer_v2 import extract_answers
from FAQs.question_generator import get_questions
from FAQs.get_gold_answer import get_gold_answer
from FAQs.qa_ranker import generate_qa_pairs

@app.route('/api',methods=['GET','POST'])
def FAQGenerator():
	if request.method=="POST":
		context=request.form['context']
		context=context.replace("\n","")
		qa_dict=extract_answers(context)
		get_questions(qa_dict)
		get_gold_answer(qa_dict)
		QAs=generate_qa_pairs(qa_dict)
		return jsonify(QAs)

