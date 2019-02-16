from mycroft import MycroftSkill, intent_file_handler


class Wutang(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('wutang.intent')
    def handle_wutang(self, message):
        self.speak_dialog('wutang')


def create_skill():
    return Wutang()

