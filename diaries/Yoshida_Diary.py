from diaries.AbstractDiary import AbstractDiary

class Yoshida_Diary(AbstractDiary):
    def get_date(self):
        return "2022-12-14"
    def get_summary(self):
        return "今日は楽しみにしていたライブ。おもしろすぎた。"
    def get_author(self):
        return "よしだ"