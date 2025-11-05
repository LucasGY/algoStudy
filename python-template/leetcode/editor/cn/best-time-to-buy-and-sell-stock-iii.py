#
# @lc app=leetcode.cn id=123 lang=python3
# @lcpr version=30301
#
# [123] 买卖股票的最佳时机 III
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_k = 2
        n = len(prices)
        dp = [[[0] * 2 for _ in range(max_k + 1)] for _ in range(n)]
        for i in range(n):
            for k in range(1,max_k+1):
                if i - 1 == -1:
                    # 处理 base case
                    dp[i][k][0] = 0
                    dp[i][k][1] = -prices[i]
                    continue
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])
        # 穷举了 n × max_k × 2 个状态，正确。
        return dp[n - 1][max_k][0]
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# [3,3,5,0,0,3,1,4]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,3,4,5]\n
# @lcpr case=end

# @lcpr case=start
# [7,6,4,3,1]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

