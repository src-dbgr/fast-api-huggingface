from urllib.request import urlopen
import pandas as pd
from transformers import pipeline
import platform
print(platform.python_version())

#from pip import _internal
#import tensorflow as tf
#tf.test.gpu_device_name()
#from transformers import pipeline

#task_bearer = pipeline("text-classification")
#summarizer = pipeline("summarization")

class Model:
        
    def __init__(self, task, model):
        if(len(model)==0):
            self.task_bearer = pipeline(task)
        if(task == 'summarization'):
            self.summarizer = pipeline(task,model=model)
        else:
            self.task_bearer = pipeline(task,model=model)

    def predict(self, text):
        outputs = self.task_bearer(text)
        return pd.DataFrame(outputs)
    
    def summarize(self, text):
        outputs = self.summarizer(text, max_length=50, clean_up_tokenization_spaces=True, truncating=True)
        return pd.DataFrame(outputs)

def get_default_task():
    return Model("text-classification","")

def get_custom_task(custom_task):
    return Model(custom_task)

def get_custom_task_and_model(custom_task,model):
    return Model(custom_task,model)

def get_summarization_and_model(model):
    return Model('summarization',model)


#classifier = pipeline("text-classification")

# outputs = classifier(text)
# print(pd.DataFrame(outputs))
