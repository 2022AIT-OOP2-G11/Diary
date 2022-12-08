from diaries.AbstractDiary import AbstractDiary


class maenodiary(AbstractDiary):

    def get_date(self):
     return "2021-12-09"

    def get_summary(self):
        return """今日はオブジェクト指向での初のグループワークでした。足を引っ張りそうで申し訳ないです、、、"""

    def get_author(self):
        return "Maeno"