def is_safe(board, row, col, n):
    # Check this column on upper rows
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper diagonal on the right side
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(board, row, n, results):
    # If all queens are placed
    if row >= n:
        results.append([row[:] for row in board])
        return

    # Try placing this queen in all columns one by one
    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1  # Place the queen
            solve_n_queens(board, row + 1, n, results)  # Recur to place rest of the queens
            board[row][col] = 0  # Backtrack (remove the queen)

def print_solution(results, n):
    for result in results:
        for row in result:
            print(" ".join("Q" if x == 1 else "." for x in row))
        print("\n")  # Print a blank line between solutions

def n_queens(n):
    # Create an NxN chessboard initialized with 0s
    board = [[0 for _ in range(n)] for _ in range(n)]
    results = []
    solve_n_queens(board, 0, n, results)
    return results

# Example usage
n = 8  # Change this value for different N
solutions = n_queens(n)
print(f"Number of solutions for {n}-Queens: {len(solutions)}")
print_solution(solutions, n)
