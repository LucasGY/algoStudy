#
# @lc app=leetcode.cn id=72 lang=python3
# @lcpr version=30203
#
# [72] 编辑距离
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)
        self.memo = [[-1] * n for _ in range(m)]
        return self.dp(word1, m-1, word2, n-1)
    
    def dp(self, s1: str, i: int, s2: str, j: int) -> int:
        if i == -1:
            return j + 1
        if j == -1:
            return i + 1

        # 查备忘录，避免重叠子问题
        if self.memo[i][j] != -1:
            return self.memo[i][j]

        # 状态转移，结果存入备忘录
        if s1[i] == s2[j]:
            self.memo[i][j] = self.dp(s1, i - 1, s2, j - 1)
        else:
            self.memo[i][j] = min(
                self.dp(s1, i, s2, j - 1) + 1,
                self.dp(s1, i - 1, s2, j) + 1,
                self.dp(s1, i - 1, s2, j - 1) + 1
            )

        return self.memo[i][j]


        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# "horse"\n"ros"\n
# @lcpr case=end

# @lcpr case=start
# "intention"\n"execution"\n
# @lcpr case=end

#

