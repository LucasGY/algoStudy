#
# @lc app=leetcode.cn id=213 lang=python3
# @lcpr version=30300
#
# [213] 打家劫舍 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        self.memo = [[-1] * n for _ in range(n)]
        if n == 1:
            return nums[0]
        return max(self.robRange(nums, 0, n - 2), self.robRange(nums, 1, n - 1))
    
    def robRange(self, nums, start, end):
        if start > end:
            return 0
        if start == end:
            return nums[start]

        if self.memo[start][end] != -1:
            return self.memo[start][end]
        
        res = max(
            nums[start] + self.robRange(nums, start + 2, end),
            self.robRange(nums, start + 1, end)
        )
        
        self.memo[start][end] = res

        return res


        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# [2,3,2]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3]\n
# @lcpr case=end

#

