class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph = {i: [] for i in range(numCourses)}

        for a, b in prerequisites:
            graph[a].append(b)
        
        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if graph[crs] == []:
                return True
            
            visited.add(crs)

            for preq in graph[crs]:
                if not dfs(preq):
                    return False
            visited.remove(crs)
            graph[crs] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

