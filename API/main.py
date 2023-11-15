from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
from model import predict

app = FastAPI()

class post_data(BaseModel):
	customer_id : int

@app.get('/')
async def root():
    return {"Message": "Welcome to Score Prediction API."}

@app.post("/predict")
def score(input_data:post_data):
	score = predict(input_data.customer_id)
	return {"score": score}

if __name__ == "__main__":
	uvicorn.run(app)