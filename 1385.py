from typing import List


class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        n = len(arr2)
        ans = 0
        for arr in arr1:
            left, right = 0, n - 1
            while left <= right:
                mid = (left + right) // 2
                if abs(arr - arr2[mid]) <= d:
                    ans += 1
                    break
                if arr < arr2[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
        return len(arr1) - ans
