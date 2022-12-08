from diaries.AbstractDiary import AbstractDiary

class SakaguchiDiary(AbstractDiary):
    def get_date(self):
        return "2021-12-08"
    def get_summary(self):
        return "物理実験が終わらない...徹夜を覚悟した1日だった"
    def get_author(self):
        return "Sakaguchi"