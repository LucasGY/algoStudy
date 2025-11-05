#
# @lc app=leetcode.cn id=45 lang=python3
# @lcpr version=30300
#
# [45] 跳跃游戏 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        self.memo = [n] * n
        return self.dp(nums, 0)
    
    def dp(self, nums, p):
        n = len(nums)
        if p >= n - 1:
            return 0

        steps = nums[p]
        local = n
        for i in range(1, steps+1):
            subProblem = self.dp(nums, p + i)
            local = min(local, subProblem + 1)
        return local
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# [2,3,1,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [2,3,0,1,4]\n
# @lcpr case=end

#

