
from nexus_controller import NexusController
from challenges import ChallengesManager

def main_menu():
    print("--- نظام Nexus للتحكم المركزي ---")
    print("1. تحديث مستوى VIP")
    print("2. إضافة تحدي جديد")
    print("3. خروج")

    choice = input("اختر عملية: ")
    
    if choice == '1':
        uid = input("أدخل معرف المستخدم: ")
        lvl = int(input("أدخل مستوى الـ VIP: "))
        NexusController().set_vip(uid, lvl)
        
    elif choice == '2':
        cid = input("معرف التحدي: ")
        uid = input("معرف المنشئ: ")
        rew = float(input("قيمة المكافأة: "))
        ChallengesManager().add_challenge(cid, uid, rew)
        
    else:
        print("إغلاق النظام.")

if __name__ == "__main__":
    main_menu()
