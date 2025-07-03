from app.expiry_env import ExpiryProductEnv
from stable_baselines3 import PPO
from stable_baselines3.common.callbacks import CheckpointCallback

env = ExpiryProductEnv()
checkpoint_callback = CheckpointCallback(save_freq=1000, save_path='./training/checkpoints/', name_prefix='expiry_model')
model = PPO("MlpPolicy", env, verbose=1, tensorboard_log="./ppo_logs/")
model.learn(total_timesteps=20000, callback=checkpoint_callback)
model.save("expiry_model")
print("✅ Model saved as 'expiry_model.zip'")
