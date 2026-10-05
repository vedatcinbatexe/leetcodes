"""
    4061: Minimum Queen Moves to Reach Target
    There is an 8 x 8 empty chessboard with 1-indexed rows and columns.

    You are given an array source = [sr, sc] representing the starting position of a queen, and an array target = [tr, tc] representing the target position.

    In one move, the queen travels one or more squares along a single row, column, or diagonal, staying within the board.

    Return the minimum number of moves for the queen to land exactly on target.
"""


class Solution:
    def minQueenMoves(self, source: list[int], target: list[int]) -> int:
        minMoves = 0
        
        if source == target:
            return 0
        
        if source[0] == target[0] or source[1] == target[1] or (abs(source[0] - target[0]) == abs(source[1] - target[1])):
            minMoves = 1
            
        else:
            minMoves = 2
        
        
        
        return minMoves
        



# Recommended Solution
class Solution:
    def minQueenMoves(self, source: list[int], target: list[int]) -> int:
        ax, ay = source
        bx, by = target

        dx = bx-ax
        dy = by-ay

        if dx == 0 and dy == 0:
            return 0

        if abs(dx) == abs(dy) or dx == 0 or dy == 0:
            return 1

        return 2
        