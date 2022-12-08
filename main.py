from diaries.DiarySample import DiarySample
from diaries.MakimuraDiary import MakimuraDiary
from diaries.SakaguchiDiary import SakaguchiDiary

# ↓のリストには、メンバーの各⽇記が格納されます。
diaries = [
    DiarySample(), 
    MakimuraDiary(),
    SakaguchiDiary(),
    ]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()