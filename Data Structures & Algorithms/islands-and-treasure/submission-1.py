class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        q = deque()
        distance = 0

        def checkLand(r, c):
            if r < 0 or r >= ROW or c < 0 or c >= COL or grid[r][c] == -1 or (r,c) in visited:
                return
            q.append((r, c))
            visited.add((r, c))
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 0:
                    visited.add((r, c))
                    q.append((r,c))
        
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = distance
                checkLand(r + 1, c)
                checkLand(r - 1, c)
                checkLand(r, c + 1)
                checkLand(r, c - 1)
            distance += 1

        