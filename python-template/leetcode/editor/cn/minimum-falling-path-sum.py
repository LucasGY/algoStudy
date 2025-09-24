#
# @lc app=leetcode.cn id=931 lang=python3
# @lcpr version=30203
#
# [931] 下降路径最小和
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        res = float('inf')
        self.memo = [[66666 for _ in range(n)] for _ in range(n)]
        for j in range(n):
            res = min(res, self.dp(matrix, n-1, j))
        return res
    
    def dp(self, matrix: List[List[int]], i: int, j: int) -> int:
        if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[0]):
            return 99999
        if i == 0:
            return matrix[0][j]
        if self.memo[i][j] != 66666:
            return self.memo[i][j]
        
        self.memo[i][j] = matrix[i][j] + min(
            self.dp(matrix, i - 1, j),
            self.dp(matrix, i - 1, j - 1),
            self.dp(matrix, i - 1, j + 1)
        )
        return self.memo[i][j]

        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# [[2,1,3],[6,5,4],[7,8,9]]\n
# @lcpr case=end

# @lcpr case=start
# [[-19,57],[-40,-5]]\n
# @lcpr case=end

#

