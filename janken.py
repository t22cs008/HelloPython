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

# メイン処理
def play_janken():
    a_hand = get_hand()
    b_hand = get_hand()
    
    # プレイヤーの手を表示
    print(f"Aの手: {hands[a_hand]} v.s. Bの手: {hands[b_hand]} → {judge(a_hand, b_hand)}")

# ゲームの実行
if __name__ == "__main__":
    play_janken()
