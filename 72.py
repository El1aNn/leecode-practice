# 给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)

        def dp(i, j):
            if i == 0:
                return j + 1
            if j == 0:
                return i + 1
            if word1[i-1] == word2[j-1]:
                return dp(i-1, j-1)
            else:
                return 1 + min(dp(i-1, j), dp(i, j-1), dp(i-1, j-1))
        return dp(m-1, n-1)
