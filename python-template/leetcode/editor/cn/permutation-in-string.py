#
# @lc app=leetcode.cn id=567 lang=python3
# @lcpr version=30304
#
# [567] 字符串的排列
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window, need = {}, {}
        left, right = 0, 0
        valid = 0
        for character in s1:
            need[character] = need.get(character, 0) + 1

        while right < len(s2):
            c = s2[right]
            right += 1
            
            if c in need:
                window[c] = window.get(c, 0) + 1
                if window[c] == need[c]:
                    valid += 1 

            while right - left >= len(s1):
                if valid == len(need):
                    return True
                d = s2[left]
                left += 1
                if d in need:
                    if window[d] == need[d]:
                        valid -= 1
                    window[d] -= 1
        return False

        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# "ab"\n"eidbaooo"\n
# @lcpr case=end

# @lcpr case=start
# "ab"\n"eidboaoo"\n
# @lcpr case=end

#

