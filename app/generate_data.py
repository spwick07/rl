import csv
import random

def simulate():
    with open("logs/outcomes.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        for _ in range(1000):
            units = random.randint(10, 100)
            days = random.randint(1, 10)
            cost = round(random.uniform(5, 20), 2)
            total = units * cost
            action = random.choice([0, 1, 2, 3])
            reward = {
                0: round(units * cost * random.uniform(0.3, 0.9), 2),
                1: -round(total * 0.05, 2),
                2: round(units * cost * random.uniform(0.2, 0.6), 2),
                3: -round(total * 0.5, 2) if days == 1 else 0
            }[action]
            writer.writerow([units, days, cost, total, action, reward, "simulated"])

simulate()
print("✅ Simulated 1000 samples in logs/outcomes.csv")
