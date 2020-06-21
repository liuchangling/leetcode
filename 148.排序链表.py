#
# @lc app=leetcode.cn id=148 lang=python3
#
# [148] 排序链表
#
# https://leetcode-cn.com/problems/sort-list/description/
#
# algorithms
# Medium (65.38%)
# Likes:    589
# Dislikes: 0
# Total Accepted:    67.7K
# Total Submissions: 102.9K
# Testcase Example:  '[4,2,1,3]'
#
# 在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。
# 
# 示例 1:
# 
# 输入: 4->2->1->3
# 输出: 1->2->3->4
# 
# 
# 示例 2:
# 
# 输入: -1->5->3->4->0
# 输出: -1->0->3->4->5
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 思路1 作弊利用额外空间，性能爆表99%
# 思路2 归并排序
#  查找mid 用 fast,slow 快慢双指针法，奇数个节点找到中点，偶数个节点找到中心左边的节点。
#         

class Solution:
    # 思路1  借用了额外空间的情况， 就是当做普通listsort  效率最高了。 76ms 99.9%
    def sortList(self, head: ListNode) -> ListNode:
        arr = []
        Dummy_head = new_head = head
        while head:
            arr.append(head.val)
            head = head.next
        arr = list(sorted(arr))
        for elem in  arr:
            new_head.val = elem
            new_head = new_head.next
        return Dummy_head


    # -----------------------------------------------------------------------------
    # 思路2 归并排序 224ms 73%

    # def sortList(self, head: ListNode) -> ListNode:

    #     return self.mergeSort(head)
    
    # def mergeSort(self, node:ListNode) -> ListNode:
    #     if node is None or node.next is None : return node # 递归终止条件
    #     slow = node
    #     fast = node.next

    #     # 快慢指针找mid
    #     while fast and fast.next:
    #         slow = slow.next
    #         fast = fast.next.next

    #     mid = slow.next # mid
    #     slow.next = None # 切断mid到右侧的链

    #     right = self.mergeSort(mid) # 对右侧排序        
    #     left = self.mergeSort(node) # 对左侧排序

    #     return self.mergeList(left, right)


    
    # def mergeList(self, left:ListNode, right:ListNode)-> ListNode:
    #     head = ListNode(-1)
    #     dummy = head

    #     while left and right:
    #         if left.val < right.val:
    #             dummy.next = left
    #             left = left.next
    #         else :
    #             dummy.next = right
    #             right = right.next

    #         dummy = dummy.next

    #     dummy.next = left if left else right


    #     return head.next


    # -----------------------------------------------------------------------------
    # 思路3 快速排序 TLE

    # def sortList(self, head: ListNode) -> ListNode:
    #     if head is None or head.next is None: return head

    #     dummy = ListNode(-1)
    #     dummy.next = head
    #     return self.quickSort(dummy, None)


    # def quickSort(self, start: ListNode, end: ListNode) -> ListNode:
    #     # start 总是一个dummy head ， 所以我们要比较start.next 是否和end 相等
    #     if start == end or start.next == end or start.next.next == end : return start

    #     partition = start.next
    #     tempHead = ListNode(-1)
        
    #     # partition为划分点，p为链表指针，temp为临时链表指针
    #     p = partition
    #     temp = tempHead

    #     while p.next != end:
    #         if p.next.val < partition.val: #将小于partition.val的放入临时链表
    #             temp.next = p.next
    #             temp = temp.next
    #             p.next = p.next.next # 原链表中踢掉这个节点，为了便于删除，所以我们总是用p.next.val来比较
    #         else:
    #             p = p.next

    #     # 合并临时链表和原链表，将原链表接到临时链表后面即可
    #     temp.next = start.next 

    #     # 将临时链表插回原链表，注意是插回！（不做这一步在对右半部分处理时就断链了）
    #     start.next = tempHead.next

    #     self.quickSort(start, partition)
    #     self.quickSort(partition, end)

    #     return start.next



# @lc code=end

