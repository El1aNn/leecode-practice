# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是
# 回文串。返回 s 所有可能的分割方案。
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        path = []
        n = len(s)

        def backtrack(i):
            if i == n:
                ans.append(path.copy())
                return
            for j in range(i, n):

                if s[i:j + 1] == s[i:j + 1][::-1]:
                    path.append(s[i:j + 1])
                    backtrack(j + 1)
                    path.pop()

        backtrack(0)

        return ans


s = Solution()
print(s.partition(" aab"))
