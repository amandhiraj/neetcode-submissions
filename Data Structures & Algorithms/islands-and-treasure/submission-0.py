class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS, COLS = len(grid), len(grid[0])

        v = set()
        q = deque()

        def checkLand(r, c):
            if r < 0 or r == ROWS or c < 0 or c == COLS or (r,c) in v or grid[r][c] == -1:
                return
            q.append((r, c))
            v.add((r, c))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    v.add((r, c))

        dist = 0

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                checkLand(r + 1, c)
                checkLand(r - 1, c)
                checkLand(r, c + 1)
                checkLand(r, c - 1)
                
            dist += 1
        