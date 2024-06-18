# Medical Chat Bot

### Steps

1. create and activate a virtual environment called medbot
```bash
conda create -n medbot python3.10 -y
```
```bash
conda activate medbot
```
2. Install the required packages and requirements
```bash
pip install -r requirements.txt
```
```bash
requirements
* langchain==0.0.225
* ctransformers==0.2.5
* sentence-transformers==2.2.2
* pinecone-client
* flask
```

3. Download the Llama 2, `llama-2-7b-chat.ggmlv3.q4_0.bin`, model from Hugging Face through this link:
```bash
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/blob/main/llama-2-7b-chat.ggmlv3.q4_0.bin
```
4. Create .env file in the root directory and add Pinecone credentials
```bash
PINECONE_API_KEY = "--------------------------------"
``` 

