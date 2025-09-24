#
# @lc app=leetcode.cn id=139 lang=python3
# @lcpr version=30203
#
# [139] 单词拆分
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def __init__(self):
        self.wordDict = []
        # 记录是否找到一个合法的答案
        self.found = False
        # 记录回溯算法的路径
        self.track = []
        self.memo = set()

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.wordDict = wordDict
        self.backtrack(s, 0)
        return self.found
    
    def backtrack(self, s: str, i: int):
        if self.found:
            # 如果已经找到答案，就不要再递归搜索了
            return
        if i == len(s):
            # 整个 s 都被匹配完成，找到一个合法答案
            self.found = True
            return
        
        suffix = s[i:]
        if suffix in self.memo:
            # 当前子串（子树）不能被切分，就不用继续递归了
            return

        for word in self.wordDict:
            length = len(word)
            if i + length <= len(s) and s[i:i+length] == word:
                self.track.append(word)
                self.backtrack(s, i+length)
                self.track.pop()
        
        # 后序位置，将不能切分的子串（子树）记录到备忘录
        if not self.found:
            self.memo.add(suffix)




        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# "leetcode"\n["leet", "code"]\n
# @lcpr case=end

# @lcpr case=start
# "applepenapple"\n["apple", "pen"]\n
# @lcpr case=end

# @lcpr case=start
# "catsandog"\n["cats", "dog", "sand", "and", "cat"]\n
# @lcpr case=end

#

