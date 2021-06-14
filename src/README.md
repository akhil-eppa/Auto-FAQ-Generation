* Answer Extraction Pipeline 
To use the answer extraction pipeline, create an extractor object as follows:
```
import nltk
nltk.download('punkt')
from pipelines import answer_pipeline
x=answer_pipeline("answer-extraction",ans_model="valhalla/t5-small-qa-qg-hl",ans_tokenizer="valhalla/t5-small-qa-qg-hl")
x("-------***Enter your text here***-----------")
```
