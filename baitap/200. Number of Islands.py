class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        m, n = len(grid), len(grid[0])
        count = 0

        def dfs(i, j):
            # check bounds and water
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == "0":
                return
            # mark visited
            grid[i][j] = "0"
            # explore neighbors
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    dfs(i, j)

        return count
