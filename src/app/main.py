from fastapi import FastAPI

app = FastAPI(
    title="Python Learning API",
    description="FastAPI setup for agents & services",
    version="0.1.0",
)

@app.get("/health")
def health_check():
    return {"status": "ok hai "}
