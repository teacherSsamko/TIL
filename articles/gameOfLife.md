# LeetCode - Game Of Life (Python)

## Description

[Problem Link](https://leetcode.com/problems/game-of-life/)
Medium

## Solution

```python
from itertools import product

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols = len(board), len(board[0])
        copied_board = [[board[row][col] for col in range(cols)] for row in range(rows)]
        
        moves = list(product([-1, 0, 1], repeat=2))
        moves.remove((0,0))
        
        for row in range(rows):
            for col in range(cols):
                # Get live neigbors
                neigbors = 0
                for x, y in moves:
                    x_ = col+x
                    y_ = row+y
                    if x_ < 0 or y_ < 0:
                        continue
                    try:
                        if copied_board[y_][x_] == 1:
                            neigbors += 1
                    except:
                        continue
                
                # Case 1: Live Cell
                if copied_board[row][col] == 1:
                    # Case 1-1: under-population
                    # Case 1-2: live
                    # Case 1-3: over-population
                    if neigbors < 2 or neigbors > 3:
                        board[row][col] = 0
                    else:
                        board[row][col] = 1 
                # Case 2: Dead Cell
                else:
                # Case 2-1: reproduction
                    if neigbors == 3:
                        board[row][col] = 1
```

At first, I tried to use 'next_round_board' and change the board into it. But it doesn't work. So, I changed strategy that using 'copied_origin_board' for checking origin state for the board while updating simultaneously.  

And I use product for getting all possible moves(8 directions).
Also, I use 'try' and 'except' for avoiding out of index exception. It's a faster way than using 'if' statement to validate index.
