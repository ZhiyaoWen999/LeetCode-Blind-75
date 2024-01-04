import collections
#BFS
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])
        def bfs(starts):
            directions = [(1,0),(-1,0),(0,1),(0,-1)]
            q = collections.deque(starts)
            visited = set(starts)
            while q:
                i, j = q.popleft()
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and heights[ni][nj] >= heights[i][j] and (ni, nj) not in visited:
                        visited.add((ni,nj))
                        q.append((ni,nj))
            return visited


        # The start positons
        alt = [(i,n-1) for i in range(m)] + [(m-1,i) for i in range(n)]
        pac = [(0,i) for i in range(n)] + [(i,0) for i in range(m)]
        return list(bfs(alt) & bfs(pac))


#DFS
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(row, col, visted,  preheights):
            if (row < 0 
            or row >= rows 
            or col < 0 
            or col >= cols 
            or (row, col) in visted 
            or heights[row][col] < preheights
            ):
                return
            visted.add((row, col))
            dfs(row + 1, col, visted, heights[row][col])
            dfs(row - 1, col, visted, heights[row][col])
            dfs(row, col + 1, visted, heights[row][col])
            dfs(row, col - 1, visted, heights[row][col])

        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        for i in range(rows):
            dfs(i, 0, pac, heights[i][0])
            dfs(i, cols-1, atl, heights[i][cols-1])
        for j in range(cols):
            dfs(0, j, pac, heights[0][j])
            dfs(rows-1, j, atl, heights[rows-1][j])

        res = []

        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res
    
# Time complexity : O(nm)
# Space complexity : O(nm)
