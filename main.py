import random

def SudokuSolver(board):
    empty_cell = FindEmptyCell(board)

    if not empty_cell:
        return True
    else:
        row, col = empty_cell

    for num in range(1, 10):
        if ValidMoveCheck(board, num, (row, col)):
            board[row][col] = num

            if SudokuSolver(board):
                return True

            board[row][col] = 0

    return False

def ValidMoveCheck(board, num, pos):
    row, col = pos

    for i in range(len(board[0])):
        if board[row][i] == num and col != i:
            return False

    for i in range(len(board)):
        if board[i][col] == num and row != i:
            return False

    box_start_row, box_start_col = 3 * (row // 3), 3 * (col // 3)

    for i in range(box_start_row, box_start_row + 3):
        for j in range(box_start_col, box_start_col + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True

def DisplayBoard(board):
    result = ""
    board_size = len(board)

    for i in range(board_size):
        if i % int(board_size**0.5) == 0 and i != 0:
            result += "- " * int((board_size * 1.2 + 1.2)) + "\n"

        for j in range(board_size):
            if j % int(board_size**0.5) == 0 and j != 0:
                result += "| "

            if j == board_size - 1:
                result += str(board[i][j]) + "\n"
            else:
                result += str(board[i][j]) + " "

    return result

def FindEmptyCell(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None

def GenerateBoard(difficulty, board_size):
    def FillBoard():
        base = int(board_size ** 0.5)
        side = base * base

        def pattern(r, c): return (base * (r % base) + r // base + c) % side

        def shuffle(s): return random.sample(s, len(s))

        r_base = range(base)
        rows = [g * base + r for g in shuffle(r_base) for r in shuffle(r_base)]
        cols = [g * base + c for g in shuffle(r_base) for c in shuffle(r_base)]
        nums = shuffle(range(1, base * base + 1))

        return [[nums[pattern(r, c)] for c in cols] for r in rows]

    def RemoveNumbers(board, difficulty):
        squares = side * side
        empties = squares * difficulty // 10
        for p in random.sample(range(squares), empties):
            board[p // side][p % side] = 0

    side = board_size
    board = FillBoard()

    while True:
        solved_board = [row[:] for row in board]
        if SudokuSolver(solved_board):
            break
        else:
            board = FillBoard()

    RemoveNumbers(board, difficulty)

    return board, solved_board

def UserInput(prompt, is_integer=True):
    while True:
        try:
            user_input = input(prompt)
            if is_integer:
                return int(user_input)
            else:
                return user_input
        except ValueError:
            print("Please enter a valid input.")

difficulty = UserInput("Enter difficulty level (1-9): ")
board_size = UserInput("Enter Sudoku board size (4 for 4x4, 9 for 9x9): ")

generated_board, solution = GenerateBoard(difficulty, board_size)

print("\nGenerated Sudoku Board: \n")
print(DisplayBoard(generated_board))

print("\nSudoku Board Solution: \n")
print(DisplayBoard(solution))