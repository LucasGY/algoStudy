#
# @lc app=leetcode.cn id=23 lang=python3
# @lcpr version=30302
#
# [23] 合并 K 个升序链表
#

import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from typing import *
from common.node import *
import heapq

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(-1)
        p = dummy

        pq = []
        for i, head in enumerate(lists):
            if head is not None:
                heapq.heappush(pq, (head.val, i, head))
        while pq:
            val, i, node = heapq.heappop(pq)
            p.next = node
            if node.next is not None:
                heapq.heappush(pq, (node.next.val, i, node.next))
            p = p.next
        return dummy.next

        # while True:
        #     min_index = -1
        #     min_val = float('inf')
        #     for i in range(len(lists)):
        #         if lists[i] and lists[i].val < min_val:
        #             min_val = lists[i].val
        #             min_index = i
        #     # 如果所有链表都为空，退出循环
        #     if min_index == -1:
        #         break
        #     p.next = lists[min_index]
        #     p = p.next

        #     lists[min_index] = lists[min_index].next
        # return dummy.next


        
# @lc code=end

if __name__ == '__main__':
    solution = Solution()
    # your test code here



#
# @lcpr case=start
# [[1,4,5],[1,3,4],[2,6]]\n
# @lcpr case=end

# @lcpr case=start
# []\n
# @lcpr case=end

# @lcpr case=start
# [[]]\n
# @lcpr case=end

#

