
import sqlite3

class BroadcastManager:
    def __init__(self, db_path="nexus_core.db"):
        self.db_path = db_path

    def get_all_users(self):
        conn = sqlite3.connect(self.db_path)
        users = conn.execute("SELECT id FROM users").fetchall()
        conn.close()
        return [u[0] for u in users]

    def get_vip_users(self):
        conn = sqlite3.connect(self.db_path)
        users = conn.execute("SELECT id FROM users WHERE vip_level > 0").fetchall()
        conn.close()
        return [u[0] for u in users]

    def execute_broadcast(self, target_list, message):
        print(f"جاري إرسال الرسالة إلى {len(target_list)} مستخدم...")
        for user in target_list:
            # هنا يتم ربط النظام بمنصة الرسائل أو واجهة التطبيق
            print(f"تم إرسال: '{message}' إلى {user}")
