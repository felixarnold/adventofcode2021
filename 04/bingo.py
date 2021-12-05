with open('input.txt', 'r') as input:
    data = input.read().split('\n\n')

num_calls = data.pop(0).split(',')
boards = [[[
            num for num in row.split()
        ] for row in board.split('\n')
    ] for board in data
]
scoring_board_indices = list()


def check_boards(n: str):

    for board_i, board in enumerate(boards):
        if board_i in scoring_board_indices:
            continue
        for row_i, row in enumerate(board):
            if n in row:
                n_i = row.index(n)
                boards[board_i][row_i][n_i] = ''
                if check_win(board, row_i, n_i):
                    score = calc_win(board, n)
                    scoring_board_indices.append(board_i)
                    print(score)


def check_win(board, row_i, n_i):
    if all(v == '' for v in board[row_i]):
        return True
    if all(row[n_i] == '' for row in board):
        return True
    return False


def calc_win(board, n):
    sum = 0
    for row in board:
        for val in row:
            if not val:
                continue
            sum += int(val)
    return sum * int(n)


for n in num_calls:
    check_boards(n)
