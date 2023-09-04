#Hangman

def hangman(word):
    wrong = 0
    stages = ["",
              "______      ",
              "|    |   ",
              "|    O   ",
              "|   /|\  ",
              "|   / \  ",
              "|   ",
              "----------"
              ]
    rletters=list(word)
    board=["__"]*len(word)
    win=False
    print("Welcome to Hangman")
    print(" ".join(board))
    while wrong < len(stages)-1:
        print("\n")
        msg = "Guess a letter: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind]=char
            rletters[cind]='$'
        else:
            wrong += 1
        print((" ".join(board)))
        e=wrong+1
        print("\n".join(stages[0:e]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("You lose! It was {}.".format(word))

import random

rint = random.randint(0,10)

randomword = ["hello", "cat", "dog", "water", "cute", "screen", "clothes", "couch", "van", "cup"]

hangman(randomword[rint])
