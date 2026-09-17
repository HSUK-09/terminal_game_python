from map import Map
from player import Player

def main():

    flag = True
    clear = False
    point = 0

    print("==COR==")
    player_name = input("名前を入力してください：")
    player = Player(name= player_name)
    player.show()
    print("===============================")
    map = Map(1, 1)
    map.show()
    player.status(point= point)
    key = input("キー入力：")
    map.move(key= key)

    while flag:
        for i in map.scan():
            if i == "G":
                clear = True
                flag = False
            if i == "C":
                map.map_lists[map.now_h][map.now_w] = "Ｃ"
                point += 1
                
        print("\033[17A\033[K", end="")#カーソルのをマップの上に戻す。
        map.show()
        player.status(point= point)
        key = input("キー入力：")
        map.move(key= key)

        if key == "q":
            flag = False

    if clear:
        print("ゲームクリア！")
    
if __name__ == "__main__":
    main()