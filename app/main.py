from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, FastAPI with Docker and GitHub Actions! from Sneha's side checking AGAIN DOCKER  "}
