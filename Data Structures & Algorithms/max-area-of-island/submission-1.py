from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])

        def dfs(i, j):
            # Check boundaries and if the cell is land
            if i < 0 or i >= ROW or j < 0 or j >= COL or grid[i][j] != 1:
                return 0
            
            # Mark the cell as visited
            grid[i][j] = 0

            # Initialize area for this cell
            area = 1

            # Explore neighbors
            area += dfs(i, j + 1)
            area += dfs(i + 1, j)
            area += dfs(i, j - 1)
            area += dfs(i - 1, j)

            return area

        max_area = 0
        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 1:
                    # Calculate area of the current island
                    max_area = max(max_area, dfs(i, j))
        
        return max_area
