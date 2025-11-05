#
# @lc app=leetcode.cn id=122 lang=python3
# @lcpr version=30301
#
# [122] 买卖股票的最佳时机 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        self.dp = [[0 for i in range(2)] for j in range(n)]

        for i in range(n):
            if i-1 < 0:
                self.dp[i][0] = 0
                self.dp[i][1] = -prices[i]
                continue
        
            self.dp[i][0] = max(
                self.dp[i-1][0],
                self.dp[i-1][1] + prices[i]
            )
            self.dp[i][1] = max(
                self.dp[i-1][1],
                self.dp[i-1][0]-prices[i]
            )

        return self.dp[n-1][0]
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# [7,1,5,3,6,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [7,6,4,3,1]\n
# @lcpr case=end

#

