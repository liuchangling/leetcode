#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        ret = ListNode(0)
        tmp = ret
        isTenPlus = 0

        while((not l1 is None) or (not l2 is None) or (isTenPlus ==1 )):
            # print("l1",l1 and l1.val)
            # print("l2",l2 and l2.val)
            s = 0
            l1v = 0 if (l1 is None) else l1.val
            l2v = 0 if (l2 is None) else l2.val

            s = l1v + l2v + isTenPlus
            if s >= 10 :
                isTenPlus = 1
                s = s - 10
            else :
                isTenPlus = 0

            l1 = None if (l1 is None) else l1.next
            l2 = None if (l2 is None) else l2.next

            tmp.next = ListNode(s)
            tmp = tmp.next
            # print(s)

        return ret.next

# a = ListNode(5)
# t = a
# t.next = ListNode(4)
# t = t.next
# t.next = ListNode(3)

# b = ListNode(5)
# b.next = ListNode(6)
# b.next.next = ListNode(4)

# Solution().addTwoNumbers(a, b)

# @lc code=end

