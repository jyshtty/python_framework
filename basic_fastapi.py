from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


# Run - uvicorn basic_fastapi:app --reload --host 0.0.0.0 --port 8000
# pkill -f uvicorn