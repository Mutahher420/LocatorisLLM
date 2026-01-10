from fastapi import FastAPI
from app.intelligence.industry_classifier import classify_business

app = FastAPI(title="LocatorisLLM")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/classify")
def classify(tags: dict):
    return classify_business(tags)
