def print_board(board):
    """Print the Tic-Tac-Toe board."""
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])

def check_winner(board, player):
    """Check if the current player has won."""
    win_conditions = [
        [0, 1, 2],  # Top row
        [3, 4, 5],  # Middle row
        [6, 7, 8],  # Bottom row
        [0, 3, 6],  # Left column
        [1, 4, 7],  # Center column
        [2, 5, 8],  # Right column
        [0, 4, 8],  # Diagonal (top-left to bottom-right)
        [2, 4, 6]   # Diagonal (top-right to bottom-left)
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False

def check_draw(board):
    """Check if the board is full and there is no winner."""
    return all(cell != " " for cell in board) and not (check_winner(board, "X") or check_winner(board, "O"))

def make_move(board, position, player):
    """Make a move on the board."""
    if board[position] == " ":
        board[position] = player
        return True
    return False

def get_player_move(board):
    """Get a valid move from the player."""
    while True:
        try:
            position = int(input("Enter your move (1-9): ")) - 1
            if position < 0 or position > 8:
                print("Invalid position. Choose a number between 1 and 9.")
            elif board[position] != " ":
                print("Cell already taken. Choose another position.")
            else:
                return position
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def main():
    """Main function to run the Tic-Tac-Toe game."""
    board = [" "] * 9
    current_player = "X"
    
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        print(f"Player {current_player}'s turn.")
        position = get_player_move(board)
        make_move(board, position, current_player)
        print_board(board)
        
        if check_winner(board, current_player):
            print(f"Player {current_player} wins!")
            break
        elif check_draw(board):
            print("It's a draw!")
            break
        
        # Switch player
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
