# 给你一棵 树（即一个连通、无向、无环图），根节点是节点 0 ，这棵树由编号从 0 到 n - 1 的 n 个节点组成。用下标从 0 开始、长度为 n 的数组 parent 来表示这棵树，其中 parent[i] 是节点 i 的父节点，由于节点 0 是根节点，所以 parent[0] == -1 。
#
# 另给你一个字符串 s ，长度也是 n ，其中 s[i] 表示分配给节点 i 的字符。
#
# 请你找出路径上任意一对相邻节点都没有分配到相同字符的 最长路径 ，并返回该路径的长度。
from typing import List


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        ans = 0
        n = len(parent)
        g = [[] for _ in range(n)]
        for i in range(n):
            g[parent[i]].append(i)

        def dfs(x):
            nonlocal ans
            x_len = 0
            for y in g[x]:
                y_len = dfs(y) + 1
                if s[y] != s[x]:
                    ans = max(ans, x_len + y_len)
                    x_len = max(x_len, y_len)
            return x_len

        dfs(0)
        return ans + 1
