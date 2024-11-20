from Board import Board
from cell import Cell

board = Board(9, 9, None, 0 )

for i in range(9):
    for j in range(9):
        board.grid[i][j].value = min(i, 9)
        print(board.grid[i][j].value, end = " ")
    print()
