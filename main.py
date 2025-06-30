import random

def main():
    board = create_board()
    current_symbol = "X"  # Human starts
    print_board(board)

    for _ in range(9):
        if current_symbol == "X":
            # Human move
            while True:
                row, col = get_inputs()
                if make_move(board, row, col, current_symbol):
                    break
                else:
                    print("That spot is taken. Try again.")
        else:
            print("AI is thinking...")
            ai_random_move(board, current_symbol)

        print_board(board)

        winner = check_winner(board)
        if winner:
            print(f"Winner is: {winner}")
            return
        current_symbol = "O" if current_symbol == "X" else "X"

    print("It's a tie!")


def create_board():
    board = [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"],
    ]
    return board


def ai_random_move(board, symbol):
    move = random.choice(get_available_moves(board))
    row, col = move
    make_move(board, row, col, symbol)


def make_move(board, row, col, symbol):
    if board[row][col] == "-":
        board[row][col] = symbol
        return True
    return False


def get_available_moves(board):
    empty_cells = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == "-":
                empty_cells.append((row, col))
    return empty_cells


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
