# 给你一个由 正 整数组成的数组 nums 。

# 如果数组中的某个子数组满足下述条件，则称之为 完全子数组 ：

# 子数组中 不同 元素的数目等于整个数组不同元素的数目。
# 返回数组中 完全子数组 的数目。

# 子数组 是数组中的一个连续非空序列。
from typing import Counter, List


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        m = set(nums)
        n = len(nums)
        cnt = Counter()
        ans = 0
        left = 0
        for right in range(n):
            cnt[nums[right]] += 1
            while len(cnt) == len(m):
                cnt[nums[left]] -= 1
                if cnt[nums[left]] == 0:
                    cnt.pop(nums[left])
                left += 1
            ans += left
        return ans


s = Solution()
print(s.countCompleteSubarrays([1, 2, 3, 2, 3]))  # 4
