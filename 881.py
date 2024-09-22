# 给定数组 people 。people[i]表示第 i 个人的体重 ，船的数量不限，每艘船可以承载的最大重量为 limit。
#
# 每艘船最多可同时载两人，但条件是这些人的重量之和最多为 limit。
#
# 返回 承载所有人所需的最小船数
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0
        small = 0
        big = len(people) - 1
        people.sort()
        while small <= big:
            if people[big] + people[small] > limit:
                big -= 1
                ans += 1
            else:
                big -= 1
                small += 1
                ans += 1
        return ans


S = Solution()
print(S.numRescueBoats([3,2,2,1], 3))
