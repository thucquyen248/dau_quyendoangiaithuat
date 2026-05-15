class Solution:
    def calculateMinimumHP(self, dungeon):
        m, n = len(dungeon), len(dungeon[0])
        dp = [[0] * n for _ in range(m)]

        # Base case: bottom-right cell
        dp[-1][-1] = max(1, 1 - dungeon[-1][-1])

        # Fill last row
        for j in range(n - 2, -1, -1):
            dp[-1][j] = max(1, dp[-1][j + 1] - dungeon[-1][j])

        # Fill last column
        for i in range(m - 2, -1, -1):
            dp[i][-1] = max(1, dp[i + 1][-1] - dungeon[i][-1])

        # Fill the rest
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                need = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(1, need - dungeon[i][j])

        return dp[0][0]
