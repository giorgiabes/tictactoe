def main():
    board = create_board()
    count = 0
    print_board(board)
    while True:
        player = get_current_player(count)
        print(f"Player {player}'s turn")
        row, col = get_inputs()
        if make_move(board, row, col, player):
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

def create_board():
    return [["-" for _ in range(3)] for _ in range(3)]

def make_move(board, row, col, symbol):
    if board[row][col] == "-":
        board[row][col] = symbol
        return True
    return False

def get_inputs():
    while True:
        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter col (0-2): "))
            if 0 <= row <= 2 and 0 <= col <= 2:
                return row, col
            else:
                print("Row and column must be between 0 and 2.")
        except ValueError:
            print("Please enter valid integers.")

def check_winner(board):
    return check_rows(board) or check_cols(board) or check_diagonals(board)

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
    print("  0 1 2")
    for i, row in enumerate(board):
        print(f"{i} {' '.join(row)}")

def get_current_player(count):
    return "X" if count % 2 == 0 else "O"

if __name__ == "__main__":
    main()
