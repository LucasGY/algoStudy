#
# @lc app=leetcode.cn id=140 lang=python3
# @lcpr version=30203
#
# [140] 单词拆分 II
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def __init__(self):
        # 记录结果
        self.res = []
        # 记录回溯算法的路径
        self.track = []
        self.wordDict = []

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        self.wordDict = wordDict
        # 执行回溯算法穷举所有可能的组合
        self.backtrack(s, 0)
        return self.res
    
    def backtrack(self, s: str, i: int) -> None:
        if i == len(s):
            self.res.append(' '.join(self.track))
            return 
        for word in self.wordDict:
            length = len(word)
            if i+length <= len(s) and s[i:i+length] == word:
                self.track.append(word)
                self.backtrack(s, i+length)
                self.track.pop()


        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# "catsanddog"\n["cat","cats","and","sand","dog"]\n
# @lcpr case=end

# @lcpr case=start
# "pineapplepenapple"\n["apple","pen","applepen","pine","pineapple"]\n
# @lcpr case=end

# @lcpr case=start
# "catsandog"\n["cats","dog","sand","and","cat"]\n
# @lcpr case=end

#

