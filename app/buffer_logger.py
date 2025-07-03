import csv
from datetime import datetime

def log_to_buffer(units, days, cost, total, action, reward):
    with open("logs/outcomes.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([units, days, cost, total, action, reward, datetime.now()])
