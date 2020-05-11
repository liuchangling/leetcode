#
# @lc app=leetcode.cn id=23 lang=python3
#
# [23] 合并K个排序链表
#
# https://leetcode-cn.com/problems/merge-k-sorted-lists/description/
#
# algorithms
# Hard (49.15%)
# Likes:    654
# Dislikes: 0
# Total Accepted:    119.2K
# Total Submissions: 231.4K
# Testcase Example:  '[[1,4,5],[1,3,4],[2,6]]'
#
# 合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。
# 
# 示例:
# 
# 输入:
# [
# 1->4->5,
# 1->3->4,
# 2->6
# ]
# 输出: 1->1->2->3->4->4->5->6
# 
# 思路1 分治法，每次用两个合并，直到全都合并完成，时间复杂度为 knlogk
# 思路2 维护每个链表最小的元素，每次插入一个。时间复杂度 knlogk
#       稍微有个小坑，python3对于<的比较有点问题，看下面注释吧

# @lc code=start
# Definition for singly-linked list.

import heapq

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __lt__(self,rhs):
        return self.val < rhs.val


class Solution:
    # 1 分治法
    # def mergeKLists(self, lists: List[ListNode]) -> ListNode:
    #     return self.merge(lists, 0, len(lists) - 1)
    
    # def merge(self, lists, l, r):     
    #     if l == r:
    #         return lists[l]
    #     if l > r:
    #         return None
        
    #     mid = (l + r) >> 1
    #     return self.mergeTwoLists(self.merge(lists, l, mid), self.merge(lists, mid+1, r))


    # def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    #     root = ListNode(-1)
    #     cur = root
    #     while l1 and l2:
    #         if l1.val < l2.val:
    #             cur.next = l1
    #             l1 = l1.next
    #         else: 
    #             cur.next = l2
    #             l2 = l2.next            

    #         cur = cur.next

    #     cur.next = l1 if l1 else l2
    #     return root.next

    # 2 小顶堆
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        h = []
        dummy = ListNode(-1)
        cur = dummy
        for index, node in enumerate(lists):
            if node != None:                
                # python3会顺次比较元组的多个数，因为val有重复，所以加一个index吧
                heapq.heappush(h, (node.val, index, node))
        
        while len(h)>0:
            minElem = heapq.heappop(h)
            minNode = minElem[2]
            if minNode.next:
                heapq.heappush(h, (minNode.next.val, minElem[1], minNode.next))
            
            cur.next = minNode
            cur = cur.next
        
        return dummy.next



        

# @lc code=end

