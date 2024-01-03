import collections

#DFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(i):
            # The current node has been visited by other node.
            if flags[i] == -1:
                return True
            # The current node has been visited by itself, which means there is cycle.
            if flags[i] == 1:
                return False
            # Mark current node
            flags[i] = 1

            for cur in edges[i]:
                if not dfs(cur):
                    return False
            # No cycle within current node and the node after it.
            flags[i] = -1
            
            return True

        flags = [0 for _ in range(numCourses)]

        edges = collections.defaultdict(list)

        for cur, pre in prerequisites:
            edges[pre].append(cur)
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

# BFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #The indegrees of each node, means how many prerequisites the current node have
        indegrees = [0 for _ in range(numCourses)]

        edges = collections.defaultdict(list)

        q = collections.deque()

        # Build Graph
        for cur, pre in prerequisites:
            indegrees[cur] += 1
            edges[pre].append(cur)
        
        for i in range(len(indegrees)):
            if not indegrees[i]:
                q.append(i)

        while q:
            pre = q.popleft()
            numCourses -= 1
            for cur in edges[pre]:
                indegrees[cur] -= 1
                if not indegrees[cur]:
                    q.append(cur)

        return not numCourses
