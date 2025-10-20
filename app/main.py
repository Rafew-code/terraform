from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from Day-3 pipeline (auto-deploy)", "workspace": os.getenv("TF_WORKSPACE", "local")}
