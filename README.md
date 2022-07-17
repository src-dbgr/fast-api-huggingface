# Quick and Dirty FastAPI Example
## Calling Huggingface models by passing request text via HTTP

The following list shows the dependencies I had installed to a conda virual environment

Python Version `3.9.5`

```
pip list
Package                      Version
---------------------------- ---------
absl-py                      1.1.0
anaconda                     0.0.1.1
anyio                        3.6.1
argon2-cffi                  21.3.0
argon2-cffi-bindings         21.2.0
asgiref                      3.5.2
asttokens                    2.0.5
astunparse                   1.6.3
attrs                        21.4.0
backcall                     0.2.0
beautifulsoup4               4.11.1
bleach                       5.0.1
cachetools                   5.2.0
certifi                      2022.6.15
cffi                         1.15.1
charset-normalizer           2.1.0
click                        8.1.3
colorama                     0.4.5
debugpy                      1.5.1
decorator                    5.1.1
defusedxml                   0.7.1
entrypoints                  0.4
executing                    0.8.3
fastapi                      0.79.0
fastjsonschema               2.15.3
filelock                     3.7.1
flatbuffers                  1.12
flit_core                    3.7.1
gast                         0.4.0
google-auth                  2.9.1
google-auth-oauthlib         0.4.6
google-pasta                 0.2.0
grpcio                       1.47.0
h11                          0.13.0
h5py                         3.7.0
huggingface-hub              0.8.1
idna                         3.3
importlib-metadata           4.12.0
importlib-resources          5.8.0
ipykernel                    6.9.1
ipython                      8.4.0
ipython-genutils             0.2.0
ipywidgets                   7.7.1
jedi                         0.18.1
Jinja2                       3.1.2
joblib                       1.1.0
jsonschema                   4.7.2
jupyter-client               7.2.2
jupyter-core                 4.10.0
jupyterlab-pygments          0.2.2
jupyterlab-widgets           1.1.1
keras                        2.9.0
Keras-Preprocessing          1.1.2
libclang                     14.0.1
Markdown                     3.4.1
MarkupSafe                   2.1.1
matplotlib-inline            0.1.2
mistune                      0.8.4
nbclient                     0.5.13
nbconvert                    6.5.0
nbformat                     5.4.0
nest-asyncio                 1.5.5
notebook                     6.4.12
numpy                        1.23.1
oauthlib                     3.2.0
opt-einsum                   3.3.0
packaging                    21.3
pandas                       1.4.3
pandocfilters                1.5.0
parso                        0.8.3
pickleshare                  0.7.5
pip                          22.1.2
prometheus-client            0.14.1
prompt-toolkit               3.0.20
protobuf                     3.19.4
pure-eval                    0.2.2
pyasn1                       0.4.8
pyasn1-modules               0.2.8
pycparser                    2.21
pydantic                     1.9.1
Pygments                     2.11.2
pyparsing                    3.0.9
pyrsistent                   0.18.1
python-dateutil              2.8.2
pytz                         2022.1
pywin32                      302
pywinpty                     2.0.2
PyYAML                       6.0
pyzmq                        23.2.0
regex                        2022.7.9
requests                     2.28.1
requests-oauthlib            1.3.1
rsa                          4.8
scikit-learn                 1.1.1
scipy                        1.8.1
Send2Trash                   1.8.0
sentencepiece                0.1.96
setuptools                   61.2.0
six                          1.16.0
sniffio                      1.2.0
soupsieve                    2.3.1
stack-data                   0.2.0
starlette                    0.19.1
tensorboard                  2.9.1
tensorboard-data-server      0.6.1
tensorboard-plugin-wit       1.8.1
tensorflow                   2.9.1
tensorflow-estimator         2.9.0
tensorflow-gpu               2.9.1
tensorflow-io-gcs-filesystem 0.26.0
termcolor                    1.1.0
terminado                    0.15.0
threadpoolctl                3.1.0
tinycss2                     1.1.1
tokenizers                   0.12.1
tornado                      6.1
tqdm                         4.64.0
traitlets                    5.1.1
transformers                 4.20.1
typing                       3.7.4.3
typing_extensions            4.3.0
urllib3                      1.26.10
uvicorn                      0.18.2
wcwidth                      0.2.5
webencodings                 0.5.1
Werkzeug                     2.1.2
wheel                        0.37.1
widgetsnbextension           3.6.1
wincertstore                 0.2
wrapt                        1.14.1
zipp                         3.8.1
```

Activate your conda virual environment: `conda activate <your virtual environment`
Start the server on windows: `start_server.bat` or on linux: `./start_server.sh`

Example POST request:

Example URL Pattern: `localhost:80000/model/<model-name>/task/<task name>`

URL: `localhost:8000/model/google:::pegasus-xsum/task/summarization`

- NOTE: ":::" is here a replacement for a "/" in the model name

Request Body: 
```
{
    "request_text": "It was one of the engineers, James Liang, who just did what he was told. Of course, it's not all bad—if a project you are involved in turns out to make a huge positive impact on even one person, this is going to make you feel pretty great!, Okay, so hopefully we have convinced you that you ought to care. But what should you do? As data scientists, we're naturally inclined to focus on making our models better by optimizing some metric or other. But optimizing that metric may not actually lead to better outcomes. And even if it *does* help create better outcomes, it almost certainly won't be the only thing that matters. Consider the pipeline of steps that occurs between the development of a model or an algorithm by a researcher or practitioner, and the point at which this work is actually used to make some decision. This entire pipeline needs to be considered *as a whole* if we're to have a hope of getting the kinds of outcomes we want. Normally there is a very long chain from one end to the other. This is especially true if you are a researcher, where you might not even know if your research will ever get used for anything, or if you're involved in data collection, which is even earlier in the pipeline. But no one is better placed to inform everyone involved in this chain about the capabilities, constraints, and details of your work than you are. Although there's no silver bullet that can ensure your work is used the right way, by getting involved in the process, and asking the right questions, you can at the very least ensure that the right issues are being considered., Sometimes, the right response to being asked to do a piece of work is to just say no. Often, however, the response we hear is, If I don’t do it, someone else will. But consider this: if you’ve been picked for the job, you’re the best person they’ve found to do it—so if you don’t do it, the best person isn’t working on that project. If the first five people they ask all say no too, even better!"
}
```

Example Result:
```
{
    "summary_text": {
        "0": "In our series of letters from British journalists, film-maker and columnist James Liang looks at the importance of asking the right questions."
    }
}
```


Example Console Log:

```
(my_conda_virual_env) <mypath>uvicorn main:app
3.9.5
INFO:     Started server process [8852]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
Applying Task: summarization
Applying Model: google/pegasus-xsum
2022-07-17 19:34:39.100153: I tensorflow/core/platform/cpu_feature_guard.cc:193] This TensorFlow binary is optimized with oneAPI Deep Neural Network Library (oneDNN) to use the following CPU instructions in performance-critical operations:  AVX AVX2
To enable them in other operations, rebuild TensorFlow with the appropriate compiler flags.
2022-07-17 19:34:39.502057: I tensorflow/core/common_runtime/gpu/gpu_device.cc:1532] Created device /job:localhost/replica:0/task:0/device:GPU:0 with 13620 MB memory:  -> device: 0, name: NVIDIA GeForce RTX 3080 Laptop GPU, pci bus id: 0000:01:00.0, compute capability: 8.6
2022-07-17 19:34:43.487991: I tensorflow/stream_executor/cuda/cuda_blas.cc:1786] TensorFloat-32 will be used for the matrix multiplication. This will only be logged once.
All model checkpoint layers were used when initializing TFPegasusForConditionalGeneration.

All the layers of TFPegasusForConditionalGeneration were initialized from the model checkpoint at google/pegasus-xsum.
If your task is similar to the task the model of the checkpoint was trained on, you can already use TFPegasusForConditionalGeneration for predictions without further training.
INFO:     127.0.0.1:52688 - "POST /model/google%3A%3A%3Apegasus-xsum/task/summarization HTTP/1.1" 200 OK

```