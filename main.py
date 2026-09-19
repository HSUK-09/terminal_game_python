from map import Map
from player import Player

def main():

    flag = True
    clear = False
    point = 0

    print("==COR==")
    player_name = input("名前を入力してください：")
    player = Player(name= player_name)
    map = Map(1, 1)#mapオブジェクトの作成とプレイヤーの初期位置の設定
    player.show()
    print("===============================")

    map.show()
    player.status(point= point)
    key = input("キー入力：")
    scan_res = map.scan(key= key)
    if scan_res == "G":
        clear = True
        flag = False

    if scan_res == "C":
        point += 1

    map.move(key= key)

    while flag:
        print("\033[24A\r", end="")#カーソルを上書きのためマップ左上に戻す。
        map.show()#マップの表示
        player.status(point= point)#プレイヤーのステータスの表示
        key = input("キー入力：")
        
        #特殊ブロック判定と触れた時の処理
        scan_res = map.scan(key= key)
        if scan_res == "G":
            clear = True
            flag = False

        if scan_res == "C":
            point += 1

        map.move(key= key)
        if key == "q":
            flag = False

    if clear:
        print("ゲームクリア！")
    
if __name__ == "__main__":
    main()