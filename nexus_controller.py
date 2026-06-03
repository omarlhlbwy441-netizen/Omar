
import sqlite3

class NexusController:
    DRAGON_RANKS = {
        1: "تنين البرق", 2: "تنين الجليد", 3: "تنين النار", 4: "تنين الأرض",
        5: "تنين الرياح", 6: "تنين الضوء", 7: "تنين الظل", 8: "التنين العظيم"
    }

    def __init__(self, db_path="/content/Nexus_Project/nexus_core.db"):
        self.db_path = db_path

    def upgrade_vip(self, user_id, level):
        if 1 <= level <= 8:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            cursor.execute("UPDATE users SET vip_level = ? WHERE id = ?", (level, user_id))
            conn.commit()
            conn.close()
            print(f"تم ترقية {user_id} إلى مستوى {level}: {self.DRAGON_RANKS[level]}!")
        else:
            print("خطأ: المستويات المتاحة من 1 إلى 8 فقط.")
