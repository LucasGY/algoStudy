#
# @lc app=leetcode.cn id=63 lang=python3
# @lcpr version=30203
#
# [63] 不同路径 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        self.memo = [[0] * n for _ in range(m)]
        return self.dp(obstacleGrid, m - 1, n - 1)
    
    def dp(self, grid, i, j):
        m, n = len(grid), len(grid[0])
        # base case
        if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == 1:
            # 数组越界或者遇到阻碍
            return 0
        if i == 0 and j == 0:
            # 起点到起点的路径条数就是 1
            return 1
        if self.memo[i][j] > 0:
            # 避免冗余计算
            return self.memo[i][j]
        self.memo[i][j] = self.dp(grid, i - 1, j) + self.dp(grid, i, j-1)
        return self.memo[i][j]


        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# [[0,0,0],[0,1,0],[0,0,0]]\n
# @lcpr case=end

# @lcpr case=start
# [[0,1],[0,0]]\n
# @lcpr case=end

#

