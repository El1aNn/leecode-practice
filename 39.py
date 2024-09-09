# 给你一个 无重复元素 的整数数组 candidates 和一个目标整数 target ，找出 candidates 中可以使数字和为目标数 target 的 所有 不同组合 ，并以列表形式返回。你可以按 任意顺序 返回这些组合。
#
# candidates 中的 同一个 数字可以 无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。
#
# 对于给定的输入，保证和为 target 的不同组合数少于 150 个。
from typing import List


class Solution:
    def __init__(self):
        self.result = None

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        self.result = []
        path = []

        def backtrack(i, left):
            if left == 0:
                self.result.append(path.copy())
                return
            elif left < 0 or i == len(candidates) and left < candidates[i]:
                return
            else:
                backtrack(i + 1, left)
                path.append(candidates[i])
                backtrack(i, left - candidates[i])
                path.pop()

        backtrack(0, target)
        return self.result
