import json

from fastapi import FastAPI
from fastapi.params import Query
from fastapi.responses import JSONResponse

app = FastAPI(title="Mock API")

with open("books.json", "r", encoding="utf-8") as f:
    books_data = json.load(f)


@app.get("/")
def index():
    return JSONResponse("Welcome to the Mock API")


@app.get("/books")
def get_books():
    return JSONResponse({"data": books_data["books"]})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app=app, host="0.0.0.0", reload=True)
