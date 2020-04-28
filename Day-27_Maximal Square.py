"""
Problem statement:
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:
Input: 
1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Output: 4
"""
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0]) if rows > 0 else 0
        max_square_length = 0
        
        for i in range(rows):
            for j in range(cols):
                if(matrix[i][j]) == '1':
                    square_length = 1
                    flag = True
                    while(square_length + i < rows and square_length + j < cols and flag):
                        for x in range (i, square_length+i+1):
                            if (matrix[x][j+square_length]) == '0':
                                flag = False
                                break
                        for x in range (j, square_length+j+1):
                            if (matrix[i+square_length][x]) == '0':
                                flag = False
                                break
                        if(flag):
                            square_length += 1
                    max_square_length = square_length if square_length > max_square_length else max_square_length
        return max_square_length*max_square_length
