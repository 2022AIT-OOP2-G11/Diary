from diaries.DiarySample import DiarySample
from diaries.maenodiary import maenodiary
from diaries.kuzuyatowa_diary import kuzuyatowa_diary
from diaries.NagataDiary import NagataDiary
from diaries.DoiDiary import DoiDiary
from diaries.Yoshida_Diary import Yoshida_Diary
from diaries.MakimuraDiary import MakimuraDiary
from diaries.SakaguchiDiary import SakaguchiDiary

# ↓のリストには、メンバーの各⽇記が格納されます。
diaries = [
    DiarySample(),
    DoiDiary(), 
    NagataDiary(),
    Yoshida_Diary(), 
    MakimuraDiary(),
    SakaguchiDiary(),
    kuzuyatowa_diary(),

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()