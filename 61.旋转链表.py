#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#
# https://leetcode-cn.com/problems/rotate-list/description/
#
# algorithms
# Medium (39.94%)
# Likes:    268
# Dislikes: 0
# Total Accepted:    64.8K
# Total Submissions: 160.5K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
# 
# 示例 1:
# 
# 输入: 1->2->3->4->5->NULL, k = 2
# 输出: 4->5->1->2->3->NULL
# 解释:
# 向右旋转 1 步: 5->1->2->3->4->NULL
# 向右旋转 2 步: 4->5->1->2->3->NULL
# 
# 
# 示例 2:
# 
# 输入: 0->1->2->NULL, k = 4
# 输出: 2->0->1->NULL
# 解释:
# 向右旋转 1 步: 2->0->1->NULL
# 向右旋转 2 步: 1->2->0->NULL
# 向右旋转 3 步: 0->1->2->NULL
# 向右旋转 4 步: 2->0->1->NULL
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


# 思路1 没想出来如何不借助额外空间，所以用一个额外数组处理  时间53%

# 思路2 官方有个纯指针处理的，时间居然差不多 也是53%。。。 
#      step1 遍历一次,找到尾部，tail.next = head 组成环， 同时记录长度n
#      step2 找到断开环的位置，断开即可
 

class Solution:
    # def rotateRight(self, head: ListNode, k: int) -> ListNode:
    #     array = []
    #     p = head
    #     while p:
    #         array.append(p)
    #         p = p.next
            
    #     if len(array) < 2 : return head

    #     move = k % len(array) 

    #     if move != 0:
    #         array[-move-1].next = None
    #         array[-1].next = array[0]

    #     return array[-move]
    
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None : return None

        n = 1 
        p = head
        while p.next:
            p = p.next
            n += 1
        p.next = head

        move = n - (k % n) - 1

        p = head
        while move:
            p = p.next
            move -= 1

        t = p.next
        p.next = None

        return t


        
        
        
# @lc code=end

