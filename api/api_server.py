from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from stable_baselines3 import PPO
import uvicorn

class ProductInput(BaseModel):
    units_left: int
    days_to_expiry: int
    per_unit_cost: float
    total_cost: float

app = FastAPI()
model = PPO.load("expiry_model.zip")

@app.post("/predict-strategy/")
def predict_strategy(data: ProductInput):
    obs = np.array([data.units_left, data.days_to_expiry, data.per_unit_cost, data.total_cost], dtype=np.float32)
    action, _ = model.predict(obs.reshape(1, -1))
    strategy_map = {0: "price_cut", 1: "donate", 2: "transfer", 3: "do_nothing"}
    return {"strategy": strategy_map[action]}
