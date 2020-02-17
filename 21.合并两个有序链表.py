#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (58.08%)
# Likes:    854
# Dislikes: 0
# Total Accepted:    182.5K
# Total Submissions: 305.9K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
# 示例：
# 
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# 
# 思路1 创建一个新的链表处理，空间复杂度o(n+m) 时间复杂度O(n+m) 超越了95%
# 思路2 优化一点，后续如果l1 或者l2，直接赋值。仅超越了8%  难以理解。。。这种写法为啥还会更慢？
# 思路3 不借用额外空间，直接修改l1,l2... 超越了95%
# 思路4 写法最优雅，性能较差 仅44%

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 思路1
    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     root = ListNode(-1)
    #     cur = root
    #     while l1 and l2:
    #         if l1.val < l2.val:
    #             cur.next = ListNode(l1.val)
    #             cur = cur.next                
    #             l1 = l1.next
    #         else:
    #             cur.next = ListNode(l2.val)
    #             cur = cur.next
    #             l2 = l2.next

    #     # 思路1版本
    #     while l1:
    #         cur.next = ListNode(l1.val)
    #         cur = cur.next                
    #         l1 = l1.next
        
    #     while l2:
    #         cur.next = ListNode(l2.val)
    #         cur = cur.next
    #         l2 = l2.next

    #     # 思路2版本 为何反而变慢了。。。无法理解
    #     # if l1 :
    #     #     cur.next = l1
    #     # elif l2 :
    #     #     cur.next = l2
            
    #     return root.next

    # 思路3 不生成额外节点
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # 将空间复杂度降下来
        root = ListNode(-1)
        cur = root
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else: 
                cur.next = l2
                l2 = l2.next            

            cur = cur.next

        cur.next = l1 if l1 else l2

        return root.next

    # 思路4 递归试试 性能较差
    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     if l1 is None:
    #         return l2
    #     if l2 is None:
    #         return l1

    #     if l1.val < l2.val:
    #         l1.next = self.mergeTwoLists(l1.next, l2)
    #         return l1
    #     else:
    #         l2.next = self.mergeTwoLists(l1, l2.next)
    #         return l2



# @lc code=end

