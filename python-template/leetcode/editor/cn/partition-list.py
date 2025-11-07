#
# @lc app=leetcode.cn id=86 lang=python3
# @lcpr version=30301
#
# [86] 分隔链表
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l1 = ListNode(-1)
        l2 = ListNode(-1)
        p1,p2 = l1,l2

        while head:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            head = head.next
        p2.next = None
        p1.next = l2.next
        return l1.next
        
        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# [1,4,3,2,5,2]\n3\n
# @lcpr case=end

# @lcpr case=start
# [2,1]\n2\n
# @lcpr case=end

#

