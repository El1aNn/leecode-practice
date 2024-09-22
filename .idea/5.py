class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        rs = s[::-1]
        l = len(s)
        ans = ''
        count = 0
        dp = [[0 for _ in range(l + 1)] for _ in range(l + 1)]
        for i, c1 in enumerate(s):
            for j, c2 in enumerate(rs):
                if c1 == c2:
                    if dp[i][j] == count:
                        ans = ans + c1
                        count += 1
                    dp[i + 1][j + 1] = dp[i][j] + 1

                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

        return ans


s = Solution()
print(s.longestPalindromeSubseq("asdass"))
