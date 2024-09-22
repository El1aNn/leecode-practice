# 给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
#
# 百度百科中最近公共祖先的定义为：“对于有根树 T 的两个节点 p、q，最近公共祖先表示为一个节点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find(node, path, target):
            if not node:
                return None
            x = node.val
            path.append(x)
            if x == target: return True
            if find(node.left, path, target) or find(node.right, path, target):
                return True
            path.pop()
            return False

        lq = []
        lp = []
        find(root, lq, q)
        find(root, lp, p)
        d = {}
        for _ in range(len(lq) + len(lp)):
            if lq:
                x = lq.pop()
                if x in d:
                    return x
                else:
                    d[x] = 1

            if lp:
                x = lp.pop()
                if x in d:
                    return x
                else:
                    d[x] = 1
