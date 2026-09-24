class Map:
    def __init__(self, now_h, now_w):
        self.map_lists_stage1 = [["B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B"],
                                 ["B","E","B","E","B","E","E","E","E","E","E","E","B","E","C","E","G","B"],
                                 ["B","E","B","E","B","C","B","E","B","B","B","E","B","E","B","B","B","B"],
                                 ["B","E","B","E","B","E","B","E","B","E","E","E","B","E","B","E","E","B"],
                                 ["B","E","B","E","B","E","B","E","B","E","B","B","B","E","B","E","E","B"],
                                 ["B","E","B","E","B","E","B","E","B","C","E","E","B","E","E","E","E","B"],
                                 ["B","E","B","C","E","C","B","E","B","E","B","B","B","B","B","E","E","B"],
                                 ["B","E","B","E","B","B","B","E","B","E","E","E","B","E","E","E","E","B"],
                                 ["B","E","B","E","B","E","E","E","B","E","B","C","B","E","B","E","B","B"],
                                 ["B","E","B","E","B","C","B","B","B","E","E","E","E","E","E","E","E","B"],
                                 ["B","E","B","E","B","E","B","E","E","E","B","E","B","E","B","E","B","B"],
                                 ["B","E","E","E","B","E","E","C","E","E","B","E","E","E","E","E","E","B"],
                                 ["B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B"]]
        
        self.map_lists_stage2 = [["B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B"],
                                 ["B","E","E","E","E","E","B","E","B","E","E","B","E","E","E","E","E","B"],
                                 ["B","E","B","E","E","E","E","E","E","E","E","B","E","B","B","B","E","B"],
                                 ["B","E","E","E","B","B","B","E","B","E","E","B","E","E","E","B","E","B"],
                                 ["B","B","B","E","B","E","E","E","B","B","B","B","B","E","E","B","E","B"],
                                 ["B","E","E","E","B","E","B","B","B","E","E","E","E","E","E","B","E","B"],
                                 ["B","G","B","E","E","E","E","E","B","E","B","B","E","B","E","E","E","B"],
                                 ["B","B","B","E","B","E","E","E","B","E","B","B","E","E","E","B","E","B"],
                                 ["B","E","E","E","B","E","B","E","E","E","E","B","E","B","B","E","E","B"],
                                 ["B","E","B","E","B","E","B","E","B","E","E","E","E","B","B","E","E","B"],
                                 ["B","E","B","E","E","E","B","E","B","B","B","E","E","E","E","B","E","B"],
                                 ["B","E","B","E","B","E","E","E","E","E","E","E","E","E","E","E","E","B"],
                                 ["B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B"]]
        self.now_h = now_h
        self.now_w = now_w
        self.map_lists_stage1[now_h][now_w] = "P"

        self.up = [-1, 0]
        self.down = [1, 0]
        self.right = [0, -1]
        self.left = [0, 1]


    def show(self, map_lists):
        #map_listsを読み込んで表示する

        #ブロックを追加する際はmap_blockにキーと値（マップの記号：　表示する記号）を追加
        map_block = {"E": "　", "B": "＃", "P": "ｐ", "G": "G ", "C":  "Ｃ"}
        
        for array in map_lists:
            map = ""
            for string in array:
                block = map_block[string]

                #表示する記号に色をつける
                if string == "B":
                    block = "\033[32m" + block + "\033[0m"

                elif string == "C":
                    block = "\033[33m" + block + "\033[0m"

                elif string == "P":
                    block = "\033[31m" + block + "\033[0m"

                map  += block
            print(map)

    def move(self, key, map_lists):
        #プレイヤーの移動処理
        new_h = self.now_h
        new_w = self.now_w

        map_lists[self.now_h][self.now_w] = "B"
        if key == "w" and map_lists[self.now_h - 1][self.now_w] != "B":
            new_h += self.up[0]
            new_w += self.up[1]

        elif key == "s" and map_lists[self.now_h + 1][self.now_w] != "B":
            new_h += self.down[0]
            new_w += self.down[1]
            
        elif key == "a" and map_lists[self.now_h][self.now_w - 1] != "B":
            new_h += self.right[0]
            new_w += self.right[1]

        elif key == "d"and map_lists[self.now_h][self.now_w + 1] != "B":
            new_h += self.left[0]
            new_w += self.left[1]

        self.now_h = new_h
        self.now_w = new_w
        map_lists[self.now_h][self.now_w] = "P"
        
    def scan(self, key, map_lists):
        #特殊ブロックの取得判定
        if key == "w":
            return map_lists[self.now_h-1][self.now_w]

        elif key == "s":
            return map_lists[self.now_h+1][self.now_w]
        
        elif key == "a":
            return map_lists[self.now_h][self.now_w-1]
        
        elif key == "d":
            return map_lists[self.now_h][self.now_w+1]

        else :
            return None


