# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


from typing import Optional, List


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(node, num):
            if not node: return
            if num == len(ans):
                ans.append(node.val)
            dfs(node.right, num + 1)
            dfs(node.left, num + 1)

        dfs(root, 0)
        return ans
