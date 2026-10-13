"""
EXPERIMENT 2: 8-QUEEN PROBLEM
Course: CSA17 - ARTIFICIAL INTELLIGENCE
Course Outcome: CO1
Description: Solving the 8-Queens Problem using Backtracking Algorithm.
"""

def is_safe(board, row, col, n=8):
    """Checks if a queen can be safely placed at board[row][col]."""
    # Check this row on left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on left side
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def print_board(board, n=8):
    """Prints the chessboard visually."""
    print("   " + " ".join([f"C{c}" for c in range(n)]))
    print("  +" + "---" * n + "+")
    for r in range(n):
        row_str = " ".join([" Q" if board[r][c] == 1 else " ." for c in range(n)])
        print(f"R{r}|{row_str} |")
    print("  +" + "---" * n + "+")

def solve_n_queens_all(n=8):
    """Finds all valid solutions for N-Queens problem using backtracking."""
    board = [[0] * n for _ in range(n)]
    solutions = []

    def backtrack(col):
        if col >= n:
            solutions.append([row[:] for row in board])
            return

        for row in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                backtrack(col + 1)
                board[row][col] = 0  # Backtrack

    backtrack(0)
    return solutions

if __name__ == '__main__':
    N = 8
    print("=" * 55)
    print(f" EXPERIMENT 2: SOLVING {N}-QUEENS PROBLEM USING BACKTRACKING ")
    print("=" * 55)
    print(f"Aim: Place {N} queens on an {N}x{N} chessboard such that")
    print("     no two queens attack each other.\n")

    solutions = solve_n_queens_all(N)
    print(f"Total valid non-attacking solutions found: {len(solutions)}\n")

    print("Displaying Solution 1:")
    sol1 = solutions[0]
    print_board(sol1, N)

    print("\nQueen Positions (Row, Column):")
    for r in range(N):
        for c in range(N):
            if sol1[r][c] == 1:
                print(f"  Queen {r + 1}: Row {r}, Column {c}")

    print("\nDisplaying Solution 2 (Alternative configuration):")
    sol2 = solutions[1]
    print_board(sol2, N)
    print("\nProblem solved successfully!")
