#
# @lc app=leetcode.cn id=53 lang=python3
# @lcpr version=30203
#
# [53] 最大子数组和
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left, right = 0, 0
        windowSum, maxSum = 0, float('-inf')

        while right < len(nums):
            windowSum += nums[right]
            right += 1

            maxSum = max(maxSum, windowSum)

            while windowSum < 0:
                windowSum -= nums[left]
                left += 1

        return maxSum
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# [-2,1,-3,4,-1,2,1,-5,4]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

# @lcpr case=start
# [5,4,-1,7,8]\n
# @lcpr case=end

#

