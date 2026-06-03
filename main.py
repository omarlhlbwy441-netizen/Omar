
from nexus_controller import NexusController
from challenges import ChallengesManager
from families import FamiliesManager

def main_menu():
    print("--- نظام Nexus للتحكم المركزي ---")
    print("1. تحديث مستوى VIP | 2. إضافة تحدي | 3. إدارة العائلات")
    choice = input("اختر عملية: ")
    
    if choice == '1':
        NexusController().set_vip(input("ID: "), int(input("Level: ")))
    elif choice == '2':
        ChallengesManager().add_challenge(input("C_ID: "), input("U_ID: "), float(input("Reward: ")))
    elif choice == '3':
        fm = FamiliesManager()
        sub = input("1. إنشاء عائلة | 2. ضم مستخدم: ")
        if sub == '1': fm.create_family(input("Family ID: "))
        else: fm.join_family(input("User ID: "), input("Family ID: "))
    else:
        print("إغلاق.")

if __name__ == "__main__":
    main_menu()
