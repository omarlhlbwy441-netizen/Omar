
import sqlite3

class ChallengesManager:
    def __init__(self, db_path="nexus_core.db"):
        self.db_path = db_path

    def add_challenge(self, challenge_id, creator_id, reward):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO challenges (id, creator_id, reward) VALUES (?, ?, ?)", 
                       (challenge_id, creator_id, reward))
        conn.commit()
        conn.close()
        print(f"تم إنشاء التحدي {challenge_id} بنجاح.")
