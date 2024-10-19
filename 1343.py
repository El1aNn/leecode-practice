# 给你一个整数数组 arr 和两个整数 k 和 threshold 。

# 请你返回长度为 k 且平均值大于等于 threshold 的子数组数目。
from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        sums = 0
        sums = sum(arr[:k])
        i = 0
        j = k - 1
        ans = 0
        n = len(arr)
        if sums/k >= threshold:
            ans += 1
        while j < n-1:
            j += 1
            sums = sums - arr[i] + arr[j]
            if sums/k >= threshold:
                ans += 1
            i += 1
        return ans
