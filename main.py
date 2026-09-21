from map import Map
from player import Player

def main():
    game_mode = 0
    flag = True
    clear = False
    point = 0

    print("==COR==")
    player_name = input("名前を入力してください：")
    player = Player(name= player_name)
    map = Map(1, 1)#mapオブジェクトの作成とプレイヤーの初期位置の設定
    player.show()
    print("===============================")

    map_lists = map.map_lists_stage1

    map.show(map_lists= map_lists)
    player.status(point= point)
    key = input("キー入力：")
    scan_res = map.scan(key= key, map_lists= map_lists)
    if scan_res == "G":
        clear = True
        flag = False

    if scan_res == "C":
        point += 1

    map.move(key= key, map_lists= map_lists)

    while flag:
        if game_mode == 0:
            map_lists = map.map_lists_stage1

        elif game_mode == 1:
            map_lists = map.map_lists_stage2

        print("\033[24A\r", end="")#カーソルを上書きのためマップ左上に戻す。
        map.show(map_lists= map_lists)#マップの表示
        player.status(point= point)#プレイヤーのステータスの表示
        key = input("キー入力：")
        
        #特殊ブロック判定と触れた時の処理
        scan_res = map.scan(key= key, map_lists= map_lists)
        if scan_res == "G":
            if game_mode == 0:
                game_mode = 1

            elif game_mode == 1:
                clear = True
                flag = False

        if scan_res == "C":
            point += 1

        map.move(key= key, map_lists= map_lists)
        if key == "q":
            flag = False

    if clear:
        print("ゲームクリア！")
    
if __name__ == "__main__":
    main()