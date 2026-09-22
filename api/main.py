from fastapi import FastAPI
from fastapi.params import Query
from fastapi.responses import JSONResponse

app = FastAPI(title="Mock API")


@app.get("/")
def index():
    return JSONResponse("Welcome to the Mock API")


@app.get("/books")
def get_books():
    with open("books.json") as f:
        return JSONResponse({"data": f})


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app=app, host="0.0.0.0", reload=True)
