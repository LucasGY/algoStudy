#
# @lc app=leetcode.cn id=111 lang=python3
# @lcpr version=30203
#
# [111] 二叉树的最小深度
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        q = Deque([root])
        depth = 1

        while q:
            size = len(q)
            for _ in range(size):
                cur = q.popleft()
                if cur.left is None and cur.right is None:
                    return depth
                if cur.left is not None:
                    q.append(cur.left)
                if cur.right is not None:
                    q.append(cur.right)
            depth += 1
        return depth
        # self.min_depth = float('inf')
        # self.cur_depth = 0
        # def dfs(root: Optional[TreeNode]):
            
        #     if root is None:
        #         return
        #     self.cur_depth += 1

        #     if (root.left is None) and (root.right is None):
        #         self.min_depth = min(self.min_depth, self.cur_depth)

        #     dfs(root.left)
        #     dfs(root.right)
        #     self.cur_depth -= 1

        # dfs(root)
        # return self.min_depth

        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [2,null,3,null,4,null,5,null,6]\n
# @lcpr case=end

#

