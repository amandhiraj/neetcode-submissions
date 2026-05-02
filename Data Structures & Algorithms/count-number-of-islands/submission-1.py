class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW, COL = len(grid), len(grid[0])

        def dfs(i, j):
            
            #set boundries
            if i < 0 or i >= ROW or j < 0 or j >= COL or grid[i][j] != '1':
                return

            grid[i][j] = '0'

            dfs(i, j + 1)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i - 1, j)
        
        island = 0
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == '1':
                    island += 1
                    dfs(i,j)
        return island

        