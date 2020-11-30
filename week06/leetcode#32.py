class Solution:
    def longestValidParentheses(self, s: str) -> int:

        maxans = 0
        dp = [0] * len(s)
        for i in range(len(s)):
            if s[i] == ")":
                if i < 1: continue
                if s[i - 1] == "(":
                    dp[i] = (dp[i - 2] if i >= 2 else 0) + 2
                elif s[i - dp[i - 1] - 1] == "(" and i - dp[i - 1] > 0:
                    dp[i] = (dp[i - dp[i - 1] - 2] if i - dp[i - 1] >= 2 else 0) + dp[i - 1] + 2
                maxans = max(maxans, dp[i])
        return maxans