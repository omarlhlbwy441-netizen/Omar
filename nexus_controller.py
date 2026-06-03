
import sqlite3

class NexusController:
    def __init__(self, db_path="nexus_core.db"):
        self.db_path = db_path

    def set_vip(self, user_id, level):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET vip_level = ? WHERE id = ?", (level, user_id))
        conn.commit()
        conn.close()
        print(f"تم ترقية {user_id} إلى مستوى VIP {level}")

    def get_user_data(self, user_id):
        conn = sqlite3.connect(self.db_path)
        data = conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
        conn.close()
        return data
