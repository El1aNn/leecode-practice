class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)
        if m + n != len(s3):
            return False

        @cache
        def dfs(i, j):
            if i < 0 and j < 0:
                return True
            if i < 0:
                return s2[:j+1] == s3[:j+1]
            if j < 0:
                return s1[:i+1] == s3[:i+1]
            if dfs(i - 1, j) and s1[i] == s3[i + j + 1]:
                return True
            if dfs(i, j - 1) and s2[j] == s3[i + j + 1]:
                return True
            return False
        return dfs(m - 1, n - 1)
