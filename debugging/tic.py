#!/usr/bin/python3

def print_board(board):
    """
    Print the current state of the board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Check if there's a winner in the game.
    """
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Check columns
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def is_full(board):
    """
    Check if the board is full.
    """
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    """
    Main function to play the game.
    """
    board = [[" "]*3 for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")

        # Get and validate input
        try:
            row = int(input("Enter row (0, 1, or 2): "))
            col = int(input("Enter column (0, 1, or 2): "))

            if row not in range(3) or col not in range(3):
                print("Invalid input. Please enter a number between 0 and 2.")
                continue

            if board[row][col] != " ":
                print("That spot is already taken! Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # Make the move
        board[row][col] = current_player

        # Check for winner
        if check_winner(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        # Check for tie
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    tic_tac_toe()
