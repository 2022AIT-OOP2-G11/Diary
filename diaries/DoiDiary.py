from diaries.AbstractDiary import AbstractDiary

class DoiDiary(AbstractDiary):

    def get_date(self):
        return "2022-12-08"

    def get_summary(self):
        return """今日は、とても寒かった。"""

    def get_author(self):
        return "Doi"