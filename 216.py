# 找出所有相加之和为 n 的 k 个数的组合，且满足下列条件：
#
# 只使用数字1到9
# 每个数字 最多使用一次
# 返回 所有可能的有效组合的列表 。该列表不能包含相同的组合两次，组合可以以任何顺序返回。
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        path = []

        def backtrack(i, left):
            if left < 0 or len(path) > k:
                return
            elif left == 0 and len(path) == k:
                ans.append(path.copy())
            else:
                for j in range(i, 10):
                    path.append(j)
                    backtrack(j + 1, left - j)
                    path.pop()

        backtrack(1, n)
        return ans


s = Solution()
print(s.combinationSum3(3, 9))
