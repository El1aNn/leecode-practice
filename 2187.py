from typing import List


class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def check(t):
            total = 0
            for i in time:
                total += (t // i)
            return total < totalTrips
        left = 0
        right = max(time) * totalTrips

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                left = mid + 1
            else:
                right = mid - 1
        return left


s = Solution()
print(s.minimumTime([1, 2, 3], 5))  # 3
