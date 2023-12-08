from fastapi import FastAPI, Request

app = FastAPI()


@app.post('/predict')
def predict(request: Request, data: dict) -> dict:
    return {
        "message": data,
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )

