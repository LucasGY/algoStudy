#
# @lc app=leetcode.cn id=55 lang=python3
# @lcpr version=30300
#
# [55] 跳跃游戏
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        return self.dp(nums, 0)
    
    def dp(self, nums, i):
        n = len(nums)
        if i >= n-1:
            return True
        for j in range(1, nums[i]+1):
            sub = self.dp(nums, i+j)
            if sub:
                return True
        return False

        # farthest = 0
        # for i in range(n-1):
        #     farthest = max(farthest, i + nums[i])
        #     if farthest >= n - 1:
        #         return True
        #     if farthest <= i:
        #         return False
        # return farthest >= n - 1

        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# [2,3,1,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [3,2,1,0,4]\n
# @lcpr case=end

#

