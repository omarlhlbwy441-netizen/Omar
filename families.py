
import sqlite3

class FamiliesManager:
    def __init__(self, db_path="nexus_core.db"):
        self.db_path = db_path

    def create_family(self, family_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO families (id) VALUES (?)", (family_id,))
        conn.commit()
        conn.close()
        print(f"تم إنشاء العائلة {family_id} بنجاح.")

    def join_family(self, user_id, family_id):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("UPDATE users SET family_id = ? WHERE id = ?", (family_id, user_id))
        conn.commit()
        conn.close()
        print(f"تم ضم المستخدم {user_id} إلى العائلة {family_id}.")

    def get_family_balance(self, family_id):
        conn = sqlite3.connect(self.db_path)
        total = conn.execute("SELECT SUM(balance) FROM users WHERE family_id = ?", (family_id,)).fetchone()[0]
        conn.close()
        return total if total else 0
