# Sudoku Solver using Backtracking Algorithm

This Python script provides a CLI Sudoku puzzle generator and solver using backtracking algorithm. It is designed to offer a hands-on experience in implementing and understanding the intricacies of backtracking while solving Sudoku puzzles.

<br/> 

## Sudoku
Sudoku is a classic number-placement puzzle where the objective is to fill a square grid with numbers so that each column, each row, and each of the subgrids (also known as boxes) contain all of the numbers from 1 to 9 (or 1 to 4 for smaller puzzles) without repetition.

<br/> 

![image](https://github.com/AswinPKumar01/Sudoku-Solver/assets/118362715/620bc177-5fbf-4dee-8c13-3e07da108435)

(classic sudoku image from adobe stock)

<br/> 

## Usage
- To use the script, simply save it to your local machine and run it.
- Provide the desired difficulty level (1-9) and Sudoku board size (4 for 4x4, 9 for 9x9) when prompted in the CLI. The script will generate a Sudoku puzzle for you to solve and display both the initial puzzle and the solution.

<br/> 

## Demo

https://github.com/AswinPKumar01/Sudoku-Solver/assets/118362715/7b0fa9ef-3d89-42cc-bc1a-49ed3bc74a98

<br/> 

## Backtracking Algorithm
The heart of this Sudoku solver lies in the backtracking algorithm, a powerful technique for solving problems that involve making a sequence of decisions. In the context of Sudoku, the backtracking algorithm explores possible number placements, backtracking when it encounters an invalid move, until a valid solution is found.

I developed this script as a way to solidify my understanding of Data Structures and Algorithms (DSA), leveraging various sources to grasp the intricacies of backtracking. 

<br/> 

## Approach

- The SudokuSolver function utilizes backtracking to recursively fill in empty cells on the Sudoku board.
- It starts by finding an empty cell and attempting to place a number (1 to 9) in that cell.
- If the move is valid, the algorithm continues to the next empty cell, repeating the process.
- If a dead-end is reached (no valid moves for a particular cell), the algorithm backtracks to the previous cell and explores alternative options.
- This process continues until a solution is found or all possibilities are exhausted.

The backtracking algorithm ensures an efficient and systematic approach to solving Sudoku puzzles, making it an ideal choice for this project. The script also includes functions for checking the validity of a move (ValidMoveCheck), displaying the Sudoku board (DisplayBoard), and finding an empty cell (FindEmptyCell).

## Author

- Coded with ♥️ by [Aswin P Kumar](https://linktr.ee/aswinpkumar)
- Thanks to various resources and tutorials on Sudoku that guided me at different stages of learning
- A more updated version is coming soon
