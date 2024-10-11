import random

# じゃんけんの手の定義
hands = ["グー", "チョキ", "パー"]

# プレイヤーの手をランダムに決める
def get_hand():
    return random.randint(0, 2)

# すべてのプレイヤーの手を表示する
def display_hands(players_hands):
    for i, hand in enumerate(players_hands):
        print(f"プレイヤー{i + 1}の手: {hands[hand]}")

# 勝敗判定を行い、勝ち手とそのプレイヤーを返す
def judge(players_hands):
    unique_hands = set(players_hands)
    
    # 全員が同じ手なら引き分け
    if len(unique_hands) == 1:
        return "引き分け", []
    
    # 「グー」「チョキ」「パー」がそれぞれ存在する場合も引き分け
    if len(unique_hands) == 3:
        return "引き分け", []
    
    # 勝ち手を決定する
    if unique_hands == {0, 1}:  # グーが勝ち
        winning_hand = 0
        result = "グーが勝ち"
    elif unique_hands == {1, 2}:  # チョキが勝ち
        winning_hand = 1
        result = "チョキが勝ち"
    elif unique_hands == {0, 2}:  # パーが勝ち
        winning_hand = 2
        result = "パーが勝ち"
    
    # 勝ち手を選んだプレイヤーをリストにして返す
    winners = [i + 1 for i, hand in enumerate(players_hands) if hand == winning_hand]
    
    return result, winners

# メイン処理
def play_janken(num_players):
    # 各プレイヤーの手をランダムに決める
    players_hands = [get_hand() for _ in range(num_players)]
    
    # 各プレイヤーの手を表示
    display_hands(players_hands)
    
    # 勝敗判定
    result, winners = judge(players_hands)
    print(f"結果: {result}")
    
    if winners:
        print(f"勝者: プレイヤー {', '.join(map(str, winners))}")

# ゲームの実行
if __name__ == "__main__":
    num_players = int(input("プレイヤーの人数を入力してください: "))
    play_janken(num_players)
