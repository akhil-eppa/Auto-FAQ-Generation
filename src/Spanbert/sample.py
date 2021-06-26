#SpanBERT finetuned on Squad v1.1

from transformers import pipeline

qa_pipeline = pipeline(
    "question-answering",
    model="mrm8488/spanbert-finetuned-squadv1",
    tokenizer="mrm8488/spanbert-finetuned-squadv1"
)


response = qa_pipeline({
    'context': "He was born on 2 October 1869 and was assassinated on 30 January 1948.",
    'question': "When was he killed?"
})

print(response)
