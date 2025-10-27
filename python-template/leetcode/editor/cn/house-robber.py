#
# @lc app=leetcode.cn id=198 lang=python3
# @lcpr version=30300
#
# [198] 打家劫舍
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        self.memo = [-1] * len(nums)
        return self.dp(nums, 0)
    
    def dp(self, nums, start):
        if start >= len(nums):
            return 0
        
        if self.memo[start] != -1:
            return self.memo[start]

        res = max(
            self.dp(nums, start + 1),
            nums[start] + self.dp(nums, start+2)
        )
        self.memo[start] = res
        return res
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# [1,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [2,7,9,3,1]\n
# @lcpr case=end

#

