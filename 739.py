# 给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        n = len(temperatures)
        # stack.append((temperatures[-1], n - 1))
        for i in range(len(temperatures)-1, -1, -1):
            while stack and temperatures[i] >= stack[-1][0]:
                stack.pop()
            answer[i] = stack[-1][1] - i if stack else 0
            stack.append((temperatures[i], i))

        return answer


s = Solution()
print(s.dailyTemperatures([89, 62, 70, 58, 47, 47, 46, 76, 100, 70]))
