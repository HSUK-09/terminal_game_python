class Player:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(self.name)

    def status(self, point):
        print("==========")
        print(f"名前：{self.name}\n"\
            + f"ポイント：{point}")