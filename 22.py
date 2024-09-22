# 数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且 有效的 括号组合。
from typing import List

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(l, r, n, path):
            if l == r == n:
                res.append("".join(path))
                return
            if l < n:
                new_path = path.copy()  # 创建 path 的拷贝
                new_path.append("(")
                backtrack(l + 1, r, n, new_path)

            if r < l:
                new_path = path.copy()  # 创建 path 的拷贝
                new_path.append(")")
                backtrack(l, r + 1, n, new_path)

        backtrack(0, 0, n, [])

        return res

    # def generateParenthesis1(self, n: int) -> List[str]:
    #     ans = []
    #
    #     def backtrack(path, a, b):
    #         if a + b == 2 * n:
    #             ans.append(''.join(path))
    #         if a < n:
    #             path.append("(")
    #             backtrack(path, a + 1, b)
    #             path.pop()
    #         if b < a:
    #             path.append(")")
    #             backtrack(path, a, b + 1)
    #             path.pop()
    #
    #     backtrack([], 0, 0)
    #     return ans


s = Solution()
print(s.generateParenthesis(3))
