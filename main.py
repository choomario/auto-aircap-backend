from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI on Render!"}

class PredictRequest(BaseModel):
    input_text: str

@app.post("/predict")
def predict(request: PredictRequest):
    # 예시 응답 (여기서 실제 처리 로직으로 교체 가능)
    return {"result": f"Prediction for: {request.input_text}"}