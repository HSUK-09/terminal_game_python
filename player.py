class Player:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"{self.name}、あなたは通路が閉じる魔法の迷路に閉じ込められてしまいました\n")

    def status(self, point):
        print("==========")
        print(f"名前：{self.name}\n"\
            + f"ポイント：{point}\n"\
            +  "=操作方法= =各種ブロック説明=\n"\
            +  "up:    w | \033[32m＃\033[0m:  壁    \n"\
            +  "down:  s | \033[33mＣ\033[0m:  コイン\n"\
            +  "right: d | G :  ゴール\n"\
            +  "left:  a |\n"\
            +  "移動方向を押してEnter\n")