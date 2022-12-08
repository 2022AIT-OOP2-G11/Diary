from diaries.DiarySample import DiarySample
from diaries.Yoshida_Diary import Yoshida_Diary

# ↓のリストには、メンバーの各⽇記が格納されます。
diaries = [
    DiarySample(), 
    Yoshida_Diary(), 
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()