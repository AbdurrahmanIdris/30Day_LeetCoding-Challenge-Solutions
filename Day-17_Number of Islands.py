"""
Problem Statement:
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input:
11110
11010
11000
00000
Output: 1

Example 2:
Input:
11000
11000
00100
00011
Output: 3
"""
#I've used the Depth-First search algorithm. I wasn't know about it before this problem. So, I'm very thankful for LeetCode 
#because each challenge add new thing to my knowledge.

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        length1 = len(grid)
        length2 = len(grid[0])
        count = 0
        
        def DepthFirst(grid,i,j):
            if i<0 or j<0 or i>length1-1 or j >length2-1 or grid[i][j] != '1':
                return            
            grid[i][j] = '#'
            DepthFirst(grid,i+1,j)
            DepthFirst(grid,i-1,j)
            DepthFirst(grid,i,j+1)
            DepthFirst(grid,i,j-1)
        
        for i in range(length1):
            for j in range(length2):
                if grid[i][j] == '1':
                    DepthFirst(grid,i,j)
                    count += 1                    
        return count
