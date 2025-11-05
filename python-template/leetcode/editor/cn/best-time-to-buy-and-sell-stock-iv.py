#
# @lc app=leetcode.cn id=188 lang=python3
# @lcpr version=30300
#
# [188] 买卖股票的最佳时机 IV
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if n <= 0:
            return 0
        # if k > n // 2:
        #     # 复用之前交易次数 k 没有限制的情况
        #     return self.maxProfit_k_inf(prices)
        
        dp = [[[0] * 2 for _ in range(k + 1)] for _ in range(n)]
        # k = 0 时的 base case
        for i in range(n):
            dp[i][0][1] = -float("inf")
            dp[i][0][0] = 0

        for i in range(n):
            for k_ in range(1, k+1):
                if i-1 < 0:
                    # 处理 i = -1 时的 base case
                    dp[i][k_][0] = 0
                    dp[i][k_][1] = -prices[i]
                    continue
                
                dp[i][k_][0] = max(
                    dp[i-1][k_][0],
                    dp[i-1][k_][1] + prices[i] 
                )
                dp[i][k_][1] = max(
                    dp[i-1][k_][1],
                    dp[i-1][k_-1][0] - prices[i]
                )

        return dp[n-1][k][0]
    # def maxProfit_k_inf(self, prices: List[int]) -> int:
        
        
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# 2\n[2,4,1]\n
# @lcpr case=end

# @lcpr case=start
# 2\n[3,2,6,5,0,3]\n
# @lcpr case=end

#

