#
# @lc app=leetcode.cn id=337 lang=python3
# @lcpr version=30300
#
# [337] 打家劫舍 III
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.memo = {}

    def rob(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        if root in self.memo:
            return self.memo[root]
        
        do = root.val + \
            (0 if root.left is None else self.rob(root.left.left) + self.rob(root.left.right)) +\
            (0 if root.right is None else self.rob(root.right.left) + self.rob(root.right.right))
        not_do = self.rob(root.left) + self.rob(root.right)
        res = max(do, not_do)
        self.memo[root] = res
        return res


# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# [3,2,3,null,3,null,1]\n
# @lcpr case=end

# @lcpr case=start
# [3,4,5,1,3,null,1]\n
# @lcpr case=end

#

