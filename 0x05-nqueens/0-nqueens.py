#!/usr/bin/python3
"""
N Queens Problem Solver
"""
import sys


def is_safe(board, row, col, N):
    """ Check if it's safe to place a queen at board[row][col] """
    # Check this row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    # Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens_util(board, col, N, solutions):
    """ Utility function to solve the N Queens problem """
    # If all queens are placed, then add the solution
    if col >= N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return
    
    # Consider this column and try placing this queen in all rows one by one
    for i in range(N):
        if is_safe(board, i, col, N):
            # Place this queen in board[i][col]
            board[i][col] = 1
            
            # Recur to place the rest of the queens
            solve_nqueens_util(board, col + 1, N, solutions)
            
            # If placing queen in board[i][col] doesn't lead to a solution,
            # then remove the queen (backtrack)
            board[i][col] = 0


def solve_nqueens(N):
    """ Solve the N Queens problem """
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_nqueens_util(board, 0, N, solutions)
    return solutions


def main():
    """ Main function to handle input and output """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
