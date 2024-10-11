"""じゃんけんを行うプログラムを作成する
"""
import random

# じゃんけんの手の定義
hands = ["グー", "チョキ", "パー"]

# プレイヤーAとプレイヤーBの手をランダムに決める
def get_hand():
    return random.randint(0, 2)

# 勝敗判定を行う
def judge(a_hand, b_hand):
    if a_hand == b_hand:
        return "引き分け"
    elif (a_hand == 0 and b_hand == 1) or (a_hand == 1 and b_hand == 2) or (a_hand == 2 and b_hand == 0):
        return "Aの勝ち"
    else:
        return "Bの勝ち"

# 1回のじゃんけんを行う
def play_janken():
    a_hand = get_hand()
    b_hand = get_hand()
    
    # 勝敗判定
    result = judge(a_hand, b_hand)
    
    # プレイヤーの手と結果を表示
    print(f"Aの手: {hands[a_hand]} v.s. Bの手: {hands[b_hand]} → {result}")
    
    return result

# 勝敗が決まるまでじゃんけんを行う
def best_of_three_without_draw():
    a_wins = 0
    b_wins = 0
    
    # どちらかが2回勝つまでループ
    while a_wins < 2 and b_wins < 2:
        result = play_janken()
        
        if result == "Aの勝ち":
            a_wins += 1
        elif result == "Bの勝ち":
            b_wins += 1
        
        print(f"現在のスコア - A: {a_wins}, B: {b_wins}")
    
    # 最終的な勝者の決定
    if a_wins == 2:
        print("Aが勝ちました！")
    else:
        print("Bが勝ちました！")

# ゲームの実行
if __name__ == "__main__":
    best_of_three_without_draw()
