class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Build the graph as an adjacency list
        course_graph = defaultdict(list)
        for course, prereq in prerequisites:
            course_graph[course].append(prereq)
        
        # States for each course: 0 = unvisited, 1 = visiting, 2 = fully processed
        state = [0] * numCourses
        
        def has_cycle(course):
            """
            Perform DFS to check for cycles in the graph.
            Returns True if a cycle is detected, otherwise False.
            """
            if state[course] == 1:  # Course is being visited in the current path -> cycle
                return True
            if state[course] == 2:  # Course already fully processed -> no cycle here
                return False
            
            # Mark course as being visited
            state[course] = 1
            
            # Check all prerequisites of this course
            for prereq in course_graph[course]:
                if has_cycle(prereq):
                    return True
            
            # Mark course as fully processed
            state[course] = 2
            return False
        
        # Check all courses for cycles
        for course in range(numCourses):
            if has_cycle(course):
                return False
        
        return True
