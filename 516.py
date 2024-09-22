# 给你一个字符串 s ，找出其中最长的回文子序列，并返回该序列的长度。
#
# 子序列定义为：不改变剩余字符顺序的情况下，删除某些字符或者不删除任何字符形成的一个序列。
from functools import cache


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        rs = s[::-1]
        l = len(s)

        # @cache
        # def dfs(i, j):
        #     if i < 0 or j < 0:
        #         return 0
        #     if s[i] == rs[j]:
        #         return dfs(i - 1, j - 1) + 1
        #     else:
        #         return max(dfs(i - 1, j), dfs(i, j - 1))
        #
        # return dfs(l - 1, l - 1)
        dp = [[0 for _ in range(l + 1)] for _ in range(l + 1)]
        for i, c1 in enumerate(s):
            for j, c2 in enumerate(rs):
                if c1 == c2:
                    dp[i + 1][j + 1] = dp[i][j] + 1

                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1])

        return dp[l][l]


s = Solution()

print(s.longestPalindromeSubseq("asada"))
# nums = [2, 3, 1, 3, 13, 1]
# sum = 0
# x = 0
# for y in nums:
#     sum = max(x + y, sum)
#     x = max(x, y)
# print(sum)
