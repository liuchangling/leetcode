#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
# https://leetcode-cn.com/problems/reverse-linked-list/description/
#
# algorithms
# Easy (67.48%)
# Likes:    791
# Dislikes: 0
# Total Accepted:    169.4K
# Total Submissions: 250.9K
# Testcase Example:  '[1,2,3,4,5]'
#
# 反转一个单链表。
# 
# 示例:
# 
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
# 
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 思路1 迭代法 速度94%
# 思路很简单，记录prev和head，并临时保存next
# 一顿操作之后 prev和head右移一位即可。 
# 思路2 递归法 速度83%
# 通过递归找到最后一个元素，然后和倒数第二个做逆序操作。直到head或head.next为空

class Solution:
    # 迭代法
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        while head:
            next = head.next
            head.next = prev
            prev = head
            head = next
        return prev
    
    # 递归法
    # def reverseList(self, head: ListNode) -> ListNode:
    #     if head == None or head.next == None:
    #         return head
    #     # cur 指向最后一个节点, head为倒数第二个节点
    #     cur = self.reverseList(head.next)
    #     # 逆序
    #     head.next.next = head
    #     # 防止链表循环
    #     head.next = None
    #     return cur 



# @lc code=end
