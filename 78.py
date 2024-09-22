# 给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。
# 解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start, path):
            res.append(path[:])  # 将当前 path 加入结果集

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)  # 递归调用，从下一个位置开始
                path.pop()  # 回溯，撤销选择

        backtrack(0, [])
        return res


s = Solution()
print(s.subsets([1, 2, 3]))
