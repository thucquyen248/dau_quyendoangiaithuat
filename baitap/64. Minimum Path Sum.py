class Solution:
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        dp = [[0] * n for _ in range(m)]
        
        dp[0][0] = grid[0][0]
        
        # Khởi tạo hàng đầu tiên
        for j in range(1, n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        # Khởi tạo cột đầu tiên
        for i in range(1, m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        # Điền các ô còn lại
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
        
        return dp[m-1][n-1]