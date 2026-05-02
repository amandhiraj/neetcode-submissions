class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        
        max_area = 0
        def dfs(i, j):
            
            #set boundries
            if i < 0 or i >= ROW or j < 0 or j >= COL or grid[i][j] != 1:
                return 0

            grid[i][j] = 0
            return 1 + dfs(i, j + 1) + dfs(i + 1, j) + dfs(i, j - 1) + dfs(i - 1, j)

        
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    max_area = max(max_area, dfs(i, j))
        return max_area