class CheckRepeat:
    def __init__(self,repeat_id):
        self.repeat_id = repeat_id

    def checking(self):
        result = 0
        switcher = {
            1: 0,
            2: 1,
            3: 7,
            4: 30
        }
        result = switcher.get(self.repeat_id)
        return result

