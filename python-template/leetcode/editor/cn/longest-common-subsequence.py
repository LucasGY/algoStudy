#
# @lc app=leetcode.cn id=1143 lang=python3
# @lcpr version=30203
#
# [1143] 最长公共子序列
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        self.memo = [[-1] * n for _ in range(m)]
        return self.dp(text1, 0, text2, 0)
    
    def dp(self, s1: str, i: int, s2: str, j: int) -> int:
        # base case
        if i == len(s1) or j == len(s2):
            return 0
        # 如果之前计算过，则直接返回备忘录中的答案
        if self.memo[i][j] != -1:
            return self.memo[i][j]
        # 根据 s1[i] 和 s2[j] 的情况做选择
        if s1[i] == s2[j]:
            # s1[i] 和 s2[j] 必然在 lcs 中
            self.memo[i][j] = 1 + self.dp(s1, i + 1, s2, j + 1)
        else:
            # s1[i] 和 s2[j] 至少有一个不在 lcs 中
            self.memo[i][j] = max(
                self.dp(s1, i + 1, s2, j),
                self.dp(s1, i, s2, j + 1)
            )
        return self.memo[i][j]

        


        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# "abcde"\n"ace"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n"abc"\n
# @lcpr case=end

# @lcpr case=start
# "abc"\n"def"\n
# @lcpr case=end

#

