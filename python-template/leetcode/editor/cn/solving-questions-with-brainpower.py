#
# @lc app=leetcode.cn id=2140 lang=python3
# @lcpr version=30300
#
# [2140] 解决智力问题
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        self.memo = [-1] * len(questions)
        return self.dp(questions, 0)
    
    def dp(self, questions, i):
        if i >= len(questions):
            return 0
        if self.memo[i] != -1:
            return self.memo[i]

        self.memo[i] = max(
            questions[i][0] + self.dp(questions, i+questions[i][1]+1),
            self.dp(questions, i+1)
        )
        return self.memo[i]
        
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# [[3,2],[4,3],[4,4],[2,5]]\n
# @lcpr case=end

# @lcpr case=start
# [[1,1],[2,2],[3,3],[4,4],[5,5]]\n
# @lcpr case=end

#

