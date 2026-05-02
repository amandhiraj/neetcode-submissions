class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        p_que = deque()
        p_seen = set()
        
        a_que = deque()
        a_seen = set()
        
        ROWS, COLS= len(heights), len(heights[0])

        # add all the pacific COLS
        for j in range(COLS):
            p_que.append((0, j))
            p_seen.add((0, j))
        
        # add all the pacific ROWS
        for i in range(1, ROWS):
            p_que.append((i, 0))
            p_seen.add((i, 0))
        
        # add all the pacific ROWS
        for i in range(ROWS):
            a_que.append((i, COLS - 1))
            a_seen.add((i, COLS - 1))
        
        # add all the pacific COLS   
        for j in range(COLS - 1):
            a_que.append((ROWS - 1, j))
            a_seen.add((ROWS - 1, j))

        def get_coords(que, seen):
            coords = set()
            while que:
                i, j = que.popleft()
                for r, c in [(i, j + 1), (i + 1, j),(i, j - 1),(i - 1, j)]:
                    if 0 <= r < ROWS and 0 <= c < COLS and heights[r][c] >= heights[i][j] and (r, c) not in seen:
                        seen.add((r, c))
                        que.append((r, c))
            
        get_coords(p_que, p_seen)
        get_coords(a_que, a_seen)
        return list(p_seen.intersection(a_seen))    


        