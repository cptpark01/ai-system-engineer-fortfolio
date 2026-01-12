from fastapi import FastAPI
from transformers import pipeline

app = FastAPI()

classifier = pipeline("sentiment-analysis")

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/predice")
def predict(text: str):
    result = classifier(text)
    return {"result": result}