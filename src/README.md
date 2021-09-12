* Answer Extraction Pipeline 
To use the answer extraction pipeline, create an extractor object as follows:
```
import nltk
nltk.download('punkt')
from pipelines import answer_pipeline
x=answer_pipeline("answer-extraction",ans_model="valhalla/t5-small-qa-qg-hl",ans_tokenizer="valhalla/t5-small-qa-qg-hl")
x("-------***Enter your text here***-----------")
```
<hr>
<h3> Span Prediction Module </h3> 

* This essentially is a wrapper over the Answer Extraction Pipeline discussed above
* Given a passage, get sentences and corresponding answers as: 

```
from get_answer import extract_answers
print(extract_answers("This is a small test. Run these commands to test it out."))
``` 
 * Given a passage get sentences and corresponding answers along with noun phrases as:
 ```
from get_answer_v2 import extract_answers
print(extract_answers("This is a small test. Run these commands to test it out."))
``` 

Given a passage of text this function will return a list of dictionaries.
Each dictionary has the following keys: 
* 'sentence' -> Holds an individual sentence from passage 
* 'spans' -> list of spans extracted from the given passage 
* 'questions' -> an empty list initialized. Will be filled with questions from question generation module 
* 'answers' -> an empty list initialized. Will be filled with answers from answer generation module 

<hr> 

<h3> Gold Answer Extraction Module </h3> 

* Given a sentence/context and question generate answer span using spanbert based module as follows: 
```
from get_gold_answer import extract_gold_ans
res=extract_gold_ans("He was born on 2 October 1869 and was assassinated on 30 January 1948.","When was he killed?")
print("answer = ",res["answer"])
print("probabilistic score = ",res["score"])
``` 
**UPDATE** 

* Given a sentence and question generate answer span using spanbert. 
* Following this, check if the given answer phrase is a proper noun phrase. 
* If it is a proper noun phrase, get additional information from a knowledge graph. 
```
from get_gold_answer_v2 import extract_gold_ans
res,extra=extract_gold_ans("Star Wars released in 1977.","What released in 1977?")
print("answer = ",res["answer"])
print("probabilistic score = ",res["score"])
print(extra)
print("*"*50)
if extra!=None:
    print(res["answer"]+".\n"+extra)
else:
    print(res["answer"])

'''
OUTPUT:
answer =  Star Wars
probabilistic score =  0.9976034760475159
Star Wars is an American epic space opera media franchise created by George Lucas, which began with the eponymous 1977 film and quickly became a worldwide pop-culture phenomenon. 
**************************************************
Star Wars.
Star Wars is an American epic space opera media franchise created by George Lucas, which began with the eponymous 1977 film and quickly became a worldwide pop-culture phenomenon. 
'''
```


<hr>

**Requirements** 
* transformers
* sentencepiece
* torch 
* tensorflow 
* textblob 
* nltk 
* advertools




[{"sentence":"Delhi is the capital of India.","spans":["Delhi","capital"],"questions":[],"answers":[]},{Next Sentence dictionary}]
