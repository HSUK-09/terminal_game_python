class Map:
    def __init__(self, now_h, now_w):
        self.map_lists = [["B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B","B"],
                          ["B","E","B","E","B","E","E","E","E","E","E","E","B","E","C","E","E","G"],
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
        
        self.now_h = now_h
        self.now_w = now_w
        self.map_lists[now_h][now_w] = "P"

        self.up = [-1, 0]
        self.down = [1, 0]
        self.right = [0, -1]
        self.left = [0, 1]


    def show(self):
        #map_listsを読み込んで表示する

        #ブロックを追加する際はmap_blockにキーと値（マップの記号：　表示する記号）を追加
        map_block = {"E": "　", "B": "＃", "P": "ｐ", "G": "G", "C":  "Ｃ"}
        block_key_lists = list(map_block.keys())
        for array in self.map_lists:
            map = ""
            for string in array:
                for key in block_key_lists:
                    if string == key:
                        string = map_block[key]
                map  = map + string
            print(map)

    def move(self, key):
        #プレイヤーの移動処理
        new_h = self.now_h
        new_w = self.now_w

        self.map_lists[self.now_h][self.now_w] = "E"
        if key == "w" and self.map_lists[self.now_h - 1][self.now_w] != "B":
            new_h += self.up[0]
            new_w += self.up[1]

        elif key == "s" and self.map_lists[self.now_h + 1][self.now_w] != "B":
            new_h += self.down[0]
            new_w += self.down[1]
            
        elif key == "a" and self.map_lists[self.now_h][self.now_w - 1] != "B":
            new_h += self.right[0]
            new_w += self.right[1]

        elif key == "d"and self.map_lists[self.now_h][self.now_w + 1] != "B":
            new_h += self.left[0]
            new_w += self.left[1]

        self.now_h = new_h
        self.now_w = new_w
        self.map_lists[self.now_h][self.now_w] = "P"
        
    def scan(self, key):
        #特殊ブロックの取得判定
        if key == "w":
            return self.map_lists[self.now_h-1][self.now_w]

        elif key == "s":
            return self.map_lists[self.now_h+1][self.now_w]
        
        elif key == "a":
            return self.map_lists[self.now_h][self.now_w-1]
        
        elif key == "d":
            return self.map_lists[self.now_h][self.now_w+1]

        else :
            return None


