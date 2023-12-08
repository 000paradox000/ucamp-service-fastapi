from fastapi import FastAPI, Request

from model import make_prediction

app = FastAPI()


@app.post('/predict')
def predict(request: Request, data: dict) -> dict:
    results = make_prediction(data)

    return {
        "results": results,
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        app="main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )

