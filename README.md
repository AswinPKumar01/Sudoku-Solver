# Sudoku Solver using Backtracking Algorithm

This Python script provides a CLI Sudoku puzzle generator and solver using backtracking algorithm. It is designed to offer a hands-on experience in implementing and understanding the intricacies of backtracking while solving Sudoku puzzles.

An updated Sudoku Solver with GUI can be accessed [here](https://github.com/AswinPKumar01/Sudoku-Solver-with-GUI).

<br/> 

## Sudoku
Sudoku is a classic number-placement puzzle where the objective is to fill a square grid with numbers so that each column, each row, and each of the subgrids (also known as boxes) contain all of the numbers from 1 to 9 (or 1 to 4 for smaller puzzles) without repetition.

<br/> 

![image](https://github.com/AswinPKumar01/Sudoku-Solver/assets/118362715/620bc177-5fbf-4dee-8c13-3e07da108435)

_(classic sudoku image from adobe stock)_

<br/> 

## Usage
1. Save the script to your local machine.
2. Run the script.
3. When prompted, enter the desired difficulty level (1-9) and Sudoku board size (4 for 4x4, 9 for 9x9).
4. The script will generate a Sudoku puzzle for you to solve and display both the initial puzzle and the solution.
   
<br/> 

## Function Descriptions

- **SudokuSolver**: The main function that utilizes backtracking to recursively fill in empty cells on the Sudoku board.
- **ValidMoveCheck**: Checks if a move is valid by examining the row, column, and box constraints.
- **DisplayBoard**: Creates a visual representation of the Sudoku board.
- **FindEmptyCell**: Finds the first empty cell on the Sudoku board.
- **GenerateBoard**: Generates a Sudoku board with a solution and removes numbers based on difficulty.

<br/> 

## Performance Measurement

The script includes a function, `measure_solver_performance`, which measures the time taken by the `SudokuSolver` function to solve a Sudoku puzzle.

<br/> 

## Demo

https://github.com/AswinPKumar01/Sudoku-Solver/assets/118362715/151c3c49-627e-4b6a-a085-17fafc31f7cb

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

<br/> 

## Author

- Coded with ♥️ by [Aswin P Kumar](https://linktr.ee/aswinpkumar)

## Acknowledgments

- Thanks to various resources and tutorials on Sudoku that guided me at different stages of learning
- An updated version with GUI can be accessed [here](https://github.com/AswinPKumar01/Sudoku-Solver-with-GUI).

