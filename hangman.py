def hangman(word):
    #プレイヤー2に当てて欲しい引数：word
    #プレイヤー2が間違えた数を管理するwrong
    wrong = 0
    #吊るされた男の表示リスト
    stages = ["",
             "________        ",
             "|               ",
             "|        |      ",
             "|        0      ",
             "|       /|\     ",
             "|       / \     ",
             "|               "
              ]
    #wordを一つずつ分解したもの
    rletters = list(word)
    #プレイヤー2に見せるヒント
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman")
    while wrong < len(stages)  - 1:
        print("\n")
        msg = "1文字を予想してね："
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e =wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち")
            print(" ".join(board))
            win = True
            break
        if not win:
            print("\n".join(stages[0:wrong+1]))
            print("あなたの負け！正解は：{}.".format(word))

hangman("cat")
