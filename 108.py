# 给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵
# 平衡二叉搜索树。
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return 0