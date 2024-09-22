# 输出所有n位的二进制数
from typing import List


class Solution:
    def allBinaries(self, n: int) -> List[str]:
        res = []

        def backtrack(n, path):
            if len(path) == n:
                res.append("".join(path))
                return

            path.append('0')
            backtrack(n, path)
            path.pop()

            path.append('1')
            backtrack(n, path)
            path.pop()

        backtrack(n, [])

        return res

    def allBeforeBinaries(self, n: int) -> List[str]:
        res = []

        def backtrack(start, n, path):
            if path and "".join(path) not in res:
                res.append("".join(path))
            for i in range(start, n):
                path.append('0')
                backtrack(i + 1, n, path)
                path.pop()

                path.append('1')
                backtrack(i + 1, n, path)
                path.pop()

        backtrack(0, 4, [])
        return res


s = Solution()
print(s.allBeforeBinaries(4))
