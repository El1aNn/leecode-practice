from collections import defaultdict
from typing import List, Dict


# nums1 中数字 x 的 下一个更大元素 是指 x 在 nums2 中对应位置 右侧 的 第一个 比 x 大的元素。
#
# 给你两个 没有重复元素 的数组 nums1 和 nums2 ，下标从 0 开始计数，其中nums1 是 nums2 的子集。
#
# 对于每个 0 <= i < nums1.length ，找出满足 nums1[i] == nums2[j] 的下标 j ，并且在 nums2 确定 nums2[j] 的 下一个更大元素 。如果不存在下一个更大元素，那么本次查询的答案是 -1 。
#
# 返回一个长度为 nums1.length 的数组 ans 作为答案，满足 ans[i] 是如上所述的 下一个更大元素 。
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = nums2.copy()
        temp = []
        ans = []
        Max = -1
        for i in range(len(nums1)):
            while (len(ans) != i + 1):
                a = stack.pop()
                Max = max(Max, a)
                temp.append(a)
                if a == nums1[i] and Max > nums1[i]:
                    while len(ans) != i + 1:
                        b = temp.pop()
                        if b > nums1[i]:
                            ans.append(b)
                            temp = []
                            stack = nums2.copy()
                            Max = -1
                elif Max == nums1[i]:
                    ans.append(-1)
                    temp = []
                    stack = nums2.copy()
                    Max = -1

        return ans

    def nextGreaterElement1(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = defaultdict(lambda: -1)
        stack = []
        for num in reversed(nums2):
            while stack and stack[-1] < num:
                stack.pop()
            if stack:
                m[num] = stack[-1]
            stack.append(num)
        return [m[num] for num in nums1]


class Solution1:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d = {}
        self.nge(nums2, d)
        n = len(nums1)
        result = [0] * n
        for i in range(n):
            result[i] = d[nums1[i]]
        return result

    def nge(self, nums: List[int], d: Dict[int, int]) -> List[int]:
        n = len(nums)
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and nums[i] >= stack[-1]:
                stack.pop()
            if not stack:
                d[nums[i]] = -1
            else:
                d[nums[i]] = stack[-1]
            stack.append(nums[i])


s = Solution()
print(s.nextGreaterElement([4, 1, 2], [1, 3, 4, 2]))


