import numpy as np
import pandas as pd

def generate_data_player(n_users=100, n_weeks=8):
    np.random.seed(42)
    
    data = []
    
    for user_id in range(1, n_users + 1):
        churn_score = 0
        
        # 1. Hardware
        device_class = np.random.choice(["low", "medium", "high"], p=[0.2, 0.5, 0.3])
        
   
        if device_class == "low":
            base_fps = np.random.uniform(15, 30)
        elif device_class == "medium":
            base_fps = np.random.uniform(30, 45)
        else:
            base_fps = np.random.uniform(45, 62)
        
        decay_rate = np.random.uniform(0.95, 1)
        
        # FPS per minggu
        fps_history = []
        for week in range(n_weeks):
            avg_fps_week = base_fps * (decay_rate ** week) + np.random.uniform(-1, 1)
            fps_history.append(avg_fps_week)
        


        # 2. Gacha
        factor_pulls = round(np.random.uniform(0, 30))
        total_pulls = factor_pulls * 10
        total_ssr_char = 5
        
        if factor_pulls == 0:
            ssr_obtained = 0
        else:
            ssr_obtained = round(np.random.uniform(0, total_ssr_char))
        
        soft_pity = 80
        

        if ssr_obtained > 0 and total_pulls / ssr_obtained < soft_pity:
            churn_score += 1

        got_target_character = np.random.choice([0, 1], p=[0.7, 0.3])
        
        if got_target_character == 0:
            churn_score += 1


        
        # 3. Story
        story_progress = np.random.triangular(left=0, mode=50, right=100)
        
        if story_progress > 80 and ssr_obtained <= 1:
            churn_score += 1
        
        
        # 4. Session Time (per minggu)
        base_session = np.random.uniform(5, 15)
        session_history = []
        
        for week in range(n_weeks):
            avg_fps_week = fps_history[week]
            
            fps_effect = max(0.3, avg_fps_week / 60)
            churn_effect = max(0.2, 1 - (churn_score / 5))
            
            noise = np.random.uniform(0.8, 1.2)
            
            session_time = base_session * fps_effect * churn_effect * noise
            
            # decay kalau sudah mendekati churn
            if churn_score >= 3:
                session_time *= (0.9 ** week)
            
            session_history.append(session_time)
            

            data.append({
                "user_id": user_id,
                "week": week,
                "session_time": session_time,
                "device_class": device_class,
                "avg_fps": avg_fps_week,
                "total_pulls": total_pulls,
                "ssr_obtained": ssr_obtained,
                "got_target": got_target_character,
                "story_progress": story_progress
            })
        

        avg_fps_effect = np.mean([max(0.3, f/60) for f in fps_history])
        churn_prob = min(1, churn_score / 5 + (1 - avg_fps_effect))
        churn = 1 if np.random.rand() < churn_prob else 0

        for i in range(len(data) - n_weeks, len(data)):
            data[i]["churn"] = churn
 
    df = pd.DataFrame(data)
    
    # rounding otomatis semua float
    float_cols = df.select_dtypes(include='float').columns
    df[float_cols] = df[float_cols].round(2)
    
    return df


# Generate & save
df = generate_data_player()
df.to_csv("player-dataset.csv", index=False)

print(df.head())