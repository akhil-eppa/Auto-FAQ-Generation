# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 11:07:28 2021
@author: Akhil
"""

from typing import Optional, Dict, Union
from nltk import sent_tokenize
import torch
from transformers import(
    AutoModelForSeq2SeqLM, 
    AutoTokenizer,
    PreTrainedModel,
    PreTrainedTokenizer,
)

class AnsExtPipeline:
    def __init__(
        self,
        ans_model: PreTrainedModel,
        ans_tokenizer: PreTrainedTokenizer,
        use_cuda: bool
    ):
        
        self.tokenizer = ans_tokenizer
        self.ans_model = ans_model
        self.ans_tokenizer = ans_tokenizer

        self.device = "cuda" if torch.cuda.is_available() and use_cuda else "cpu"
  
        self.ans_model.to(self.device)


        assert self.ans_model.__class__.__name__ in ["T5ForConditionalGeneration", "BartForConditionalGeneration"]
        
        if "T5ForConditionalGeneration" in self.ans_model.__class__.__name__:
            self.model_type = "t5"
        else:
            self.model_type = "bart"

    #To call using the object directly.
    #Returns list of unique answer spans
    def __call__(self, inputs: str):
        inputs = " ".join(inputs.split())
        sents, answers = self._extract_answers(inputs)
        sent_ans=[]
        #return list containing sentence and answers
        for i in zip(sents,answers):
          sent_ans.append([i[0],i[1]])
        return sent_ans

    #Given a context sentence, extract answer spans
    #Context is annotated using <hl> tags
    #Answer spans separated by <sep> tokens
    def _extract_answers(self, context):
        sents, inputs = self._prepare_inputs_for_ans_extraction(context)
        inputs = self._tokenize(inputs, padding=True, truncation=True)
        outs = self.ans_model.generate(
            input_ids=inputs['input_ids'].to(self.device), 
            attention_mask=inputs['attention_mask'].to(self.device), 
            max_length=32,
        )
        
        dec = [self.ans_tokenizer.decode(ids, skip_special_tokens=False) for ids in outs]
        answers = [item.split('<sep>') for item in dec]
        answers = [i[:-1] for i in answers]
        
        return sents, answers
    
    def _tokenize(self,
        inputs,
        padding=True,
        truncation=True,
        add_special_tokens=True,
        max_length=512
    ):
        inputs = self.ans_tokenizer.batch_encode_plus(
            inputs, 
            max_length=max_length,
            add_special_tokens=add_special_tokens,
            truncation=truncation,
            padding="max_length" if padding else False,
            pad_to_max_length=padding,
            return_tensors="pt"
        )
        return inputs
    
    def _prepare_inputs_for_ans_extraction(self, text):
        sents = sent_tokenize(text)

        inputs = []
        for i in range(len(sents)):
            source_text = "extract answers:"
            for j, sent in enumerate(sents):
                if i == j:
                    sent = "<hl> %s <hl>" % sent
                source_text = "%s %s" % (source_text, sent)
                source_text = source_text.strip()
            #t5 based models need sentence to end with </s> tag, hence appending it
            if self.model_type == "t5":
                source_text = source_text + " </s>"
            inputs.append(source_text)

        return sents, inputs


SUPPORTED_TASKS = {
    "answer-extraction": {
        "impl": AnsExtPipeline,
        "default":{
            "model": "valhalla/t5-small-qg-hl",
            "ans_model": "valhalla/t5-small-qa-qg-hl",
        }
    }
}

def answer_pipeline(
    task: str,
    ans_model = None,
    ans_tokenizer: Optional[Union[str, PreTrainedTokenizer]] = None,
    use_cuda: Optional[bool] = True,
    **kwargs,
):
    # Retrieve the task
    if task not in SUPPORTED_TASKS:
        raise KeyError("Unknown task {}, available tasks are {}".format(task, list(SUPPORTED_TASKS.keys())))

    targeted_task = SUPPORTED_TASKS[task]
    task_class = targeted_task["impl"]

    # Use default model/config/tokenizer for the task if no model is provided
    if ans_model is None:
        ans_model = targeted_task["default"]["ans_model"]
    model=targeted_task["default"]["model"]
    
    # Try to infer tokenizer from model or config name (if provided as str)
    if ans_tokenizer is None:
        if isinstance(ans_model, str):
            print("In if condition for tokenizer")
            ans_tokenizer = ans_model
        else:
            # Impossible to guest what is the right tokenizer here
            raise Exception(
                "Impossible to guess which tokenizer to use. "
                "Please provided a PretrainedTokenizer class or a path/identifier to a pretrained tokenizer."
            )
    
    # Instantiate tokenizer if needed
    if isinstance(ans_tokenizer, (str, tuple)):
        if isinstance(ans_tokenizer, tuple):
            # For tuple we have (tokenizer name, {kwargs})
            ans_tokenizer = AutoTokenizer.from_pretrained(ans_tokenizer[0], **ans_tokenizer[1])
        else:
            ans_tokenizer = AutoTokenizer.from_pretrained(ans_tokenizer, use_fast=False)
    # Instantiate model if needed
    if isinstance(ans_model, str):
        ans_model = AutoModelForSeq2SeqLM.from_pretrained(ans_model)
    if task == "answer-extraction":
      return task_class(ans_model=ans_model,ans_tokenizer=ans_tokenizer,use_cuda=use_cuda)