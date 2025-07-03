# 🧠 Expiry RL Optimizer
This project uses a custom reinforcement learning (RL) agent to automate and optimize the decision-making process for managing near-expiry products in a retail environment.

## 🔁 Core Features
- Custom Gym environment modeling real-life expiry management.
- Strategies: Price Cut, Donate, Transfer, Do Nothing.
- FastAPI endpoint for live predictions.
- Logging and replay buffer for real-world strategy improvement.
- Auto-retraining pipeline from logs.
- Simulation data generation tool.
- Optional Streamlit UI for testing.

## 🚀 How to Use

### 1. Install requirements
```bash
pip install -r api/requirements.txt
```

### 2. Train the model
```bash
python training/train_rl_agent.py
```

### 3. Run the prediction API
```bash
uvicorn api.api_server:app --reload
```

### 4. Simulate or log real-world outcomes
```bash
python app/generate_data.py
```

### 5. Retrain the model from logs
```bash
python app/retrain_from_logs.py
```

### 6. Optional: Test via Streamlit
```bash
streamlit run dashboard/streamlit_ui.py
```
