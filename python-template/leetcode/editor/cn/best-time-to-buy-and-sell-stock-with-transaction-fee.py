#
# @lc app=leetcode.cn id=714 lang=python3
# @lcpr version=30301
#
# [714] 买卖股票的最佳时机含手续费
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        dp = [[0] * 2 for _ in range(n)]
        for i in range(n):
            if i - 1 == -1:
                # base case
                dp[i][0] = 0
                dp[i][1] = -prices[i] - fee
                #   dp[i][1]
                # = max(dp[i - 1][1], dp[i - 1][0] - prices[i] - fee)
                # = max(dp[-1][1], dp[-1][0] - prices[i] - fee)
                # = max(-inf, 0 - prices[i] - fee)
                # = -prices[i] - fee
                continue
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i] - fee)
        return dp[n - 1][0]
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# [1, 3, 2, 8, 4, 9]\n2\n
# @lcpr case=end

# @lcpr case=start
# [1,3,7,5,10,3]\n3\n
# @lcpr case=end

#

