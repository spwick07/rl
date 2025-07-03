import gym
from gym import spaces
import numpy as np

class ExpiryProductEnv(gym.Env):
    def __init__(self):
        super().__init__()
        self.observation_space = spaces.Box(low=0, high=1000, shape=(4,), dtype=np.float32)
        self.action_space = spaces.Discrete(4)
        self.state = None

    def reset(self):
        units = np.random.randint(1, 100)
        days = np.random.randint(1, 10)
        cost = np.random.uniform(5, 50)
        total = units * cost
        self.state = np.array([units, days, cost, total], dtype=np.float32)
        return self.state

    def step(self, action):
        units, days, cost, total = self.state
        strategy_effectiveness = {
            0: 0.6 + np.random.rand() * 0.2,
            1: 0.0,
            2: 0.3 + np.random.rand() * 0.1,
            3: 0.1
        }

        if action == 1:
            reward = -total * 0.1
        elif action == 2:
            reward = units * cost * strategy_effectiveness[action] * 0.9
        elif action == 0:
            reward = units * (cost * 0.8) * strategy_effectiveness[action]
        else:
            reward = units * cost * strategy_effectiveness[action] if days > 1 else -total

        done = True
        info = {"action_taken": action}
        return self.state, reward, done, info
