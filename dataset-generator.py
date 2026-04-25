import numpy as np
import pandas as pd

def player_data_generator(n_users = 100, n_weeks = 8):
    np.random.seed(42)

    data = []

    for user_id in range(1, n_users + 1):
        churn_score = 0

        # 1. HARDWARE
        device_class = np.random.choice(["low", "medium", "high"], p=[0.2, 0.5, 0.3])
        if device_class == "low":
            base_fps = np.random.uniform(15, 30)
        elif device_class == "medium":
            base_fps = np.random.uniform(30, 45)
        else:
            base_fps = np.random.uniform(45, 62)

        decay_rate = np.random.uniform(0.95, 1)
        
        # fps tiap minggu
        fps_history = []

        for week in range (n_weeks):
            avg_fps_week = base_fps * (decay_rate ** week) + np.random.uniform(-1, 1) # agar lebih random
            fps_history.append(avg_fps_week)

        # 2. GACHA



