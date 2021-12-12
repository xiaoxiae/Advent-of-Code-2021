import sys

sys.path.insert(0, "../")
from utilities import success, get_input


def mark_board(board, number):
    for line in board:
        for i in range(len(line)):
            if line[i] == number:
                line[i] = None
                return


def completed(board):
    for i in range(len(board)):
        marked = True
        for j in range(len(board[i])):
            if board[i][j] is not None:
                marked = False

        if marked:
            return True

    for i in range(len(board[0])):
        marked = True
        for j in range(len(board)):
            if board[j][i] is not None:
                marked = False

        if marked:
            return True


def board_sum(board):
    total = 0
    for i in range(len(board[0])):
        for j in range(len(board)):
            if board[i][j] is not None:
                total += board[i][j]
    return total


input = get_input(whole=True).split("\n\n")

numbers = list(map(int, input[0].split(",")))

boards = []
for board in input[1:]:
    b = []
    for line in board.splitlines():
        b.append(list(map(int, line.split())))
    boards.append(b)

completed_boards = [False] * len(boards)

for number in numbers:
    for i, board in enumerate(boards):
        mark_board(board, number)
        if completed(board):
            completed_boards[i] = True

            if all(completed_boards):
                success(board_sum(board) * number)
