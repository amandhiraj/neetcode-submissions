class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        ROW, COL = len(grid), len(grid[0])
        num_fresh = 0
        que = deque()

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j] == 2:
                    que.append((i,j))
                elif grid[i][j] == 1:
                    num_fresh += 1
        
        if num_fresh == 0:
            return 0
        
        num_min = -1

        while que:
            q_size = len(que)
            num_min += 1
            for _ in range(q_size):
                i, j = que.popleft()

                for r, c in  [(i, j + 1), (i + 1, j),(i, j - 1),(i - 1, j)]:
                    if 0 <= r < ROW and 0 <= c < COL and grid[r][c] == 1:
                        grid[r][c] = 2
                        num_fresh -= 1
                        que.append((r, c))
        
            
        if num_fresh == 0:
            return num_min
        else:
            return -1
            