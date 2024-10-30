def print_board(board: dict[str, str]) -> None:
    for i in range(3):
        for j in range(3):
            print(board[str(i) + str(j)], end=' ')
        print()


def is_game_over(board):
    for i in range(3):
        if board[str(i) + str(0)] == board[str(i) + str(1)] and board[str(i) + str(0)] == board[str(i) + str(2)] and board[str(i) + '0'] != '_' and board[str(i) + '1'] != '_' and board[str(i) + '2'] != '_':
            return True, None

    if board['00'] != '_' and board['11'] != '_' and board['22'] != '_' and board['00'] == board['11'] == board['22']:
        return True, None

    if board['02'] != '_' and board['11'] != '_' and board['20'] != '_' and board['02'] == board['11'] == board['20']:
        return True, None

    if (board['00'] != '_' and board['10'] != '_' and board['20'] != '_' and board['00'] == board['10'] == board['20']) or (board['01'] != '_' and board['11'] != '_' and board['21'] != '_' and board['01'] == board['11'] == board['21']) or (board['02'] != '_' and board['12'] != '_' and board['22'] != '_' and board['02'] == board['12'] == board['22']):
        return True, None

    spots_left = False
    for _, v in board.items():
        if v == '_':
            spots_left = True

    return (not spots_left), False


def play():
    board = { '00': '_', '01': '_', '02': '_', '10': '_', '11': '_', '12': '_', '20': '_', '21': '_', '22': '_' }
    print_board(board)
    game_over = False
    players = ['x', 'o']
    curr_player = players[0]
    num_turns = 0

    game_over, has_winner = None, None
    while True:
        placement = input('\nWhat is your choice ')
        board[placement] = curr_player
        print_board(board)
        game_over, has_winner = is_game_over(board)
        if game_over:
            break
        curr_player = players[(num_turns + 1) % 2]
        num_turns += 1

    if has_winner:
        print(f"\n{curr_player} wins!")
    else:
        print("It's a draw!")


if __name__ == '__main__':
    play()
