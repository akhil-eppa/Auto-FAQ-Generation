* Answer Extraction Pipeline 
To use the answer extraction pipeline, create an extractor object as follows:
```
import nltk
nltk.download('punkt')
from pipelines import answer_pipeline
x=answer_pipeline("answer-extraction",ans_model="valhalla/t5-small-qa-qg-hl",ans_tokenizer="valhalla/t5-small-qa-qg-hl")
x("-------***Enter your text here***-----------")
```

* Given a passage get sentences and corresponding answers as:
```
from get_answer import extract_answers
print(extract_answers("This is a small test. Run these commands to test it out."))
```

Given a passage of text this function will return a list of dictionaries.
Each dictionary has the following keys: 
* 'sentence' -> Holds an individual sentence from passage 
* 'spans' -> list of spans extarcted from the given passage 
* 'questions' -> an empty list initialized. Will be filled with questions from question generation module 
* 'answers' -> an empty list initialized. Will be filled with answers from answer generation module 

**NOTE** : Adding coherence based span extraction and integration into current module is in **progress**
