class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        if m == 0 or n == 0:
            return 0
        dp = [[0] * n for _ in range(m)]
        maxarea = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    if i == 0 or j == 0:
                        dp[i][j] = 1
                    else:
                        dp[i][j] = min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1]) + 1
                maxarea = max(maxarea,dp[i][j])
        return maxarea*maxarea