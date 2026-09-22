import json

from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

app = FastAPI(title="Mock API")

with open("api/books.json", "r", encoding="utf-8") as f:
    data = json.load(f)

books = data["books"]


@app.get("/")
def index():
    return JSONResponse("Welcome to the Mock API")


@app.get("/books")
def get_books(
    seacrh: str | None = None,
    limit: int = Query(10, ge=1, le=100),
    page: int = Query(1, get=1),
):

    results = books

    # search
    if seacrh:
        seacrh = seacrh.lower()
        results = [book for book in results if seacrh in book["title"].lower()]

    # pagination
    total = len(results)

    start = (page - 1) * limit
    end = start + limit

    results = results[start:end]

    return JSONResponse(
        {
            "items": results,
            "pagination": {
                "page": page,
                "limit": limit,
                "total": total,
                "pages": (total + limit - 1) // limit,
            },
        }
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app=app, host="0.0.0.0", reload=True)
