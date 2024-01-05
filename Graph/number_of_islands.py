import collections
#DFS
class Solution:
    def dfs(self, grid, i, j):
        n, m = len(grid), len(grid[0])
        if i < 0 or i >= n or j < 0 or j>=m or grid[i][j] == '0':
            return 0
        grid[i][j] = '0'
        self.dfs(grid, i + 1, j)
        self.dfs(grid, i , j + 1)
        self.dfs(grid, i - 1, j)
        self.dfs(grid, i, j - 1)
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.dfs(grid, i, j)
                    count += 1
        return count


#BFS
class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        def bfs(grid, i, j):
            queue = collections.deque([(i, j)])
            while queue:
                [i, j] = queue.popleft()
                if 0 <= i < n and 0 <= j < m and grid[i][j] == '1':
                    grid[i][j] = '0'
                    queue += [[i + 1, j], [i - 1, j], [i, j - 1], [i, j + 1]]
        
        count = 0
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '0': continue
                bfs(grid, i, j)
                count += 1
        return count
    
# Time complexity : O(nm)
# Space complexity : O(nm)