class Player:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"{self.name}、あなたは迷路の塔に閉じ込められてしまいました\n")

    def status(self, point):
        print("==========")
        print(f"名前：{self.name}\n"\
            + f"ポイント：{point}\n"\
            +  "=操作方法= =各種ブロック説明=\n"\
            +  "up:    w | ＃:  壁    \n"\
            +  "down:  s | Ｃ:  コイン\n"\
            +  "right: d | G :  ゴール\n"\
            +  "left:  a |\n"\
            +  "移動方向を押してEnter\n")