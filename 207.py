# 你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。
#
# 在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。
#
# 例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
# 请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。
from collections import defaultdict
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(int)
        G = [[0 for _ in range(numCourses)] for _ in range(numCourses)]
        canLearn = []
        cantLearn = []
        q = []
        for u, v in prerequisites:
            graph[u] = v
            G[u][v] = 1
        for i in range(numCourses):
            if i not in graph:
                canLearn.append(i)
        for i in range(numCourses):
            if i not in canLearn:
                q.append(i)
                while q:
                    x = q.pop(0)
                    if x in cantLearn:
                        return False
                    if x not in canLearn:
                        cantLearn.append(x)
                    for i in range(numCourses):
                        if G[x][i] == 1:
                            q.append(i)
                    # if x in graph:
                    #     q.append(graph[x])
                    if x in canLearn:
                        while cantLearn:
                            y = cantLearn.pop()
                            canLearn.append(y)
        return True if len(canLearn) == numCourses else False


s = Solution()
print(s.canFinish(3, [[0, 1], [0, 2], [1, 0]]))
