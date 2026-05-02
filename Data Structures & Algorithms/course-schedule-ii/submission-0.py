class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build the graph as an adjacency list
        course_graph = defaultdict(list)
        for course, prereq in prerequisites:
            course_graph[course].append(prereq)
        
        res = []
        # States for each course: 0 = unvisited, 1 = visiting, 2 = fully processed
        state = [0] * numCourses
        
        def has_cycle(course):
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
            res.append(course)
            return False
        
        # Check all courses for cycles
        for course in range(numCourses):
            if has_cycle(course):
                return []
        
        return res