from diaries.DiarySample import DiarySample
from diaries.NagataDiary import NagataDiary
from diaries.DoiDiary import DoiDiary
from diaries.Yoshida_Diary import Yoshida_Diary
from diaries.MakimuraDiary import MakimuraDiary
from diaries.SakaguchiDiary import SakaguchiDiary

# ↓のリストには、メンバーの各⽇記が格納されます。
diaries = [
    DiarySample(),
    DoiDiary(), 


# ↓のリストには、メンバーの各⽇記が格納されます。
diaries = [
    DiarySample(), 
    NagataDiary(),
    Yoshida_Diary(), 
    MakimuraDiary(),
    SakaguchiDiary(),
    ]


for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()