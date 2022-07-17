from operator import mod
from pickle import TRUE
from typing import Union
from fastapi import Depends, FastAPI
from numpy import true_divide
from pydantic import BaseModel
from model import Model, get_custom_task, get_custom_task_and_model, get_custom_summarization_and_model

app = FastAPI()


@app.get('/')
async def root():
    return {'message': 'Hello World'}


@app.get('/v1/ml/{ml_model}')
async def executeScript(ml_model):
    return {'ML Execution': ml_model}


@app.get('/items/')
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip: skip + limit]


class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None

class Request(BaseModel):
    request_text: str

task_list = ['test-classification','ner','question-answering','translation_en_to_de','summarization']
model_list = ['facebook/bart-large-cnn','roberta-large-mnli','distilbert-base-uncased-finetuned-sst-2-english','TFBartForConditionalGeneration', 'TFBlenderbotForConditionalGeneration', 'TFBlenderbotSmallForConditionalGeneration', 'TFEncoderDecoderModel', 'TFLEDForConditionalGeneration', 'TFMarianMTModel', 'TFMBartForConditionalGeneration', 'TFMT5ForConditionalGeneration', 'TFPegasusForConditionalGeneration', 'TFT5ForConditionalGeneration','t5-small','google/pegasus-xsum']

@app.post('/model/{custom_model}/task/{task}')
async def makePrediction(request: Request, custom_model, task):
    if(len(task)==0):
        task = 'text-classification'
    if(len(custom_model)==0):
        print('Using default Model')
        custom_model = ''
    task = validateTask(task)
    custom_model = validateModel(custom_model)
    print('Applying Task: ' + task)
    print('Applying Model: ' + custom_model)
    if task == 'summarization':
        model: Model = get_custom_summarization_and_model(task,custom_model)
        return model.summarize(request.request_text)
    else:
        model: Model = get_custom_task_and_model(task,custom_model)
        return model.predict(request.request_text)

def validateTask(task):
    if task in task_list:
        return task
    else:
        print('Task: ' + task + ' is not available, taking default task')
        return 'text-classification'

def validateModel(model):
    model = model.replace(':::','/')
    if model in model_list:
        return model
    else:
        print('Model: ' + model + ' is not available, taking default model')
        return 'distilbert-base-uncased-finetuned-sst-2-english'