from diaries.AbstractDiary import AbstractDiary

class NagataDiary(AbstractDiary):
    def get_date(self):
        return "2021-12-05"
    def get_summary(self):
        return "バイトをした"
    def get_author(self):
        return "永田朋也"