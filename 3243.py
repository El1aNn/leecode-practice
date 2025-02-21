from collections import deque
from typing import List


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        m = [[i + 1] for i in range(n - 1)]
        ans = []
        vised = [-1] * n
        for i in range(len(queries)):
            isans = False
            count = 0
            m[queries[i][0]].append(queries[i][1])
            queue = deque([0])
            while queue and not isans:
                count += 1
                tmp = queue.copy()
                queue.clear()
                while tmp and not isans:
                    x = tmp.popleft()
                    for j in m[x]:
                        if vised[j] != i:
                            vised[j] = i
                            queue.append(j)
                        if j == n - 1:
                            ans.append(count)
                            isans = True
                            break
        return ans


s = Solution()
print(s.shortestDistanceAfterQueries(5, [[2, 4], [0, 2], [0, 4]]))
