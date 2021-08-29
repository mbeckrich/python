import pprint

the_board = {
    "top-L": " ",
    "top-M": " ",
    "top-R": " ",
    "mid-L": " ",
    "mid-M": " ",
    "mid-R": " ",
    "low-L": " ",
    "low-M": " ",
    "low-R": " ",
}

pprint.pprint(the_board)

""" the_board is a dictionary and when it is manipulated by having an X or O

inserted, the game of Tic Tac Toe is played. It is part of the data structure

for the game. The function below displays the data in the dictionary as a board.
"""


def print_board(board):
    print(board["top-L"] + "|" + board["top-M"] + "|" + board["top-R"])
    print("-----")
    print(board["mid-L"] + "|" + board["mid-M"] + "|" + board["mid-R"])
    print("-----")
    print(board["low-L"] + "|" + board["low-M"] + "|" + board["low-R"])


print_board(the_board)
