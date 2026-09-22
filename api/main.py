from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(title="Mock API")


@app.get("/")
def index():
    return JSONResponse("Welcome to the Mock API")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app=app, host="0.0.0.0", reload=True)
