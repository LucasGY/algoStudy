#
# @lc app=leetcode.cn id=416 lang=python3
# @lcpr version=30300
#
# [416] 分割等和子集
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        
        n = len(nums)
        target = total_sum // 2
        dp = [[False] * (target + 1) for _ in range(n + 1)]
        # base case
        for i in range(n + 1):
            dp[i][0] = True
        
        for i in range(1, n+1):
            for j in range(1, target+1):
                if j - nums[i-1] < 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j - nums[i-1]]

        return dp[n][target]
    


        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# [1,5,11,5]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,5]\n
# @lcpr case=end

#

