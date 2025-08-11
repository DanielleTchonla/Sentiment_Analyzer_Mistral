from fastapi import FastAPI, Form
import requests
app = FastAPI()

@app.get("/")
def root():
    return {"message": "Sentiment Analyzer API is running."}

@app.post("/analyze/")
def analyze_sentiment(text: str = Form(...)):
    prompt = f"What is the sentiment of this text? Respond with Positive, Negative, or Neutral:\n\n{text}"
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "mistral", "prompt": prompt, "stream": False}
    )
    result = response.json()
    return {"sentiment": result["response"].strip()}