#
# @lc app=leetcode.cn id=115 lang=python3
# @lcpr version=30203
#
# [115] 不同的子序列
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        self.memo = [[-1] * len(t) for _ in range(len(s))]
        return self.dp(s, 0, t, 0)
     
    def dp(self, s: str, i: int, t: str, j: int) -> int:
        if j == len(t):
            return 1
        if len(s) - i < len(t) - j:
            return 0
        if self.memo[i][j] != -1:
            return self.memo[i][j]
        res = 0
        if s[i] == t[j]:
            res = self.dp(s, i+1, t, j+1) + self.dp(s, i+1, t, j)
        else:
            res = self.dp(s, i+1, t, j)
        
        self.memo[i][j] = res
        return res


        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# "rabbbit"\n"rabbit"\n
# @lcpr case=end

# @lcpr case=start
# "babgbag"\n"bag"\n
# @lcpr case=end

#

