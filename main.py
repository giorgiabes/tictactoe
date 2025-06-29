def main():
    board = [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"],
    ]
    count = 0
    print_board(board)
    while True:
        row, col = get_inputs()
        if board[row][col] == "-":
            board[row][col] = get_current_player(count)
            print_board(board)
            count += 1
            winner = check_winner(board)
            if winner:
                print(f"Winner is: {winner}")
                break
            elif count > 8:
                print("Tie")
                break
        else:
            print(f"The spot {row}-{col} is taken")
            continue


def check_winner(board):
    winner = check_rows(board) or check_cols(board) or check_diagonals(board)
    return winner


def check_rows(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "-":
            return board[i][0]
    return None


def check_cols(board):
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != "-":
            return board[0][i]
    return None


def check_diagonals(board):
    if board[0][0] == board[1][1] == board[2][2] != "-":
        return board[1][1]
    elif board[0][2] == board[1][1] == board[2][0] != "-":
        return board[1][1]
    return None


def print_board(board):
    for row in board:
        print(" ".join(row))


def get_inputs():
    row = input("Enter row (0-2): ")
    col = input("Enter col (0-2): ")
    return int(row), int(col)


def get_current_player(count):
    if count % 2 == 0:
        return "X"
    else:
        return "O"


if __name__ == "__main__":
    main()
