from fastapi import FastAPI

app = FastAPI(title="CiteBid agent service")


@app.get("/health")
def health():
    return {"status": "ok"}
