from fastapi import FastAPI

app = FastAPI(title="LocatorisLLM")

@app.get("/health")
def health():
    return {"status": "ok"}
