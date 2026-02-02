from fastapi import FastAPI

from app.main import app


@app.get("/healthupdate")
def health_check():
    return {"status": "ok hai "}