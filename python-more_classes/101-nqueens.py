#!/usr/bin/python3
import sys


def is_position_safe(board, row, col):
    """
    is_position_safe - Check if the position is safe for placing a queen
    @board: Representation of the board
    @row: Row position
    @col: Column position
    Return: True if position is safe, else False
    """
    # Check if position already exist
    for i in range(row):
        # Check the column
        if board[i] == col:
            return False
        # Check diagonal \
        if board[i] - i == col - row:
            return False
        # Check diagonal /
        if board[i] + i == col + row:
            return False
    return True


def place_queens_recursive(board, row, size, solutions):
    """
    place_queens_recursive - Recursive function using backtracking
    @board: Current board state
    @row: Current row to place queen
    @size: Size of the board
    @solutions: List to store all solutions
    """
    # Place all queens
    if row == size:
        solution = []
        for i in range(size):
            solution.append([i, board[i]])
        solutions.append(solution)
        return

    for col in range(size):
        if is_position_safe(board, row, col):
            board[row] = col
            place_queens_recursive(board, row + 1, size, solutions)
            board[row] = -1


def solve_nqueens_problem(size: int):
    """
    solve_nqueens_problem - Main solver logic for the N-Queens problem
    @size: Size of the board (N x N)
    Return: None
    """
    board = [-1] * size
    solutions = []

    place_queens_recursive(board, 0, size, solutions)

    for solution in solutions:
        print(solution)


def validate_arguments():
    """
    validate_arguments - Validate command line arguments
    Return: Size if valid, exit with status 1 on error
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        size = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if size < 4:
        print("N must be at least 4")
        sys.exit(1)

    return size


def main():
    """
    main - Main function
    Return: Void
    """
    size = validate_arguments()
    solve_nqueens_problem(size)


if __name__ == "__main__":
    main()
