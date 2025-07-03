import gym
import numpy as np
import pandas as pd
from app.expiry_env import ExpiryProductEnv
from stable_baselines3 import PPO

class ReplayEnv(ExpiryProductEnv):
    def __init__(self, dataset):
        super().__init__()
        self.dataset = dataset
        self.idx = 0

    def reset(self):
        row = self.dataset.iloc[self.idx]
        self.idx = (self.idx + 1) % len(self.dataset)
        self.state = np.array([row["units"], row["days"], row["cost"], row["total"]], dtype=np.float32)
        self.reward = row["reward"]
        self.action_taken = int(row["action"])
        return self.state

    def step(self, action):
        reward = self.reward if action == self.action_taken else self.reward * 0.5
        return self.state, reward, True, {}

df = pd.read_csv("logs/outcomes.csv", names=["units", "days", "cost", "total", "action", "reward", "time"])
env = ReplayEnv(df)
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=10000)
model.save("expiry_model")
print("✅ Retrained model saved.")
