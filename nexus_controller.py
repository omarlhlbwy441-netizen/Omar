
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

    def get_dragon_benefits(self, level):
        benefits = {
            1: "سرعة استجابة أساسية + الوصول للتحديات البرونزية",
            2: "سرعة استجابة مضاعفة + الوصول للتحديات الفضية",
            3: "أولوية في البث + خصم 10% على التحديات",
            4: "وصول كامل لكل التحديات + زيادة أرصدة",
            5: "إمكانية إرسال بث جماعي خاص",
            6: "صلاحيات إشرافية على العائلات",
            7: "إدارة كاملة للمستخدمين + حماية حساب",
            8: "صلاحيات المسؤول الأعلى (Admin) + تحكم كامل في النواة"
        }
        return benefits.get(level, "مستوى غير معروف")
