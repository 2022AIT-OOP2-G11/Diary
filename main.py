from diaries.DiarySample import DiarySample
from diaries.kuzuyatowa_diary import kuzuyatowa_diary
# ↓のリストには、メンバーの各⽇記が格納されます。
diaries = [
    DiarySample(), 
    kuzuyatowa_diary(),
    ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()