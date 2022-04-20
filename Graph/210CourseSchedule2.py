# https://leetcode.com/problems/course-schedule-ii/
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = set()
        res = []
        prereq = {}
        for req in prerequisites:
            if req[0] not in prereq:
                prereq[req[0]] = [req[1]]
            else:
                prereq[req[0]].append(req[1])


        def dfs(course, prereq, path ):
            
            print(path, course)
            if course in path:
                print('Invalid')
                return False
            path.add(course)
            if course in visited:
                return True
            if course not in prereq:
                visited.add(course)
                res.append(course)
                return True
            for req in prereq[course]:
                if not dfs(req, prereq, path):
                    return False
                path.remove(req)

            visited.add(course)
            res.append(course)
            return True
        