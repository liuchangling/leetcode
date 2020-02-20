#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#
# https://leetcode-cn.com/problems/linked-list-cycle/description/
#
# algorithms
# Easy (44.10%)
# Likes:    490
# Dislikes: 0
# Total Accepted:    110.3K
# Total Submissions: 238K
# Testcase Example:  '[3,2,0,-4]\n1'
#
# 给定一个链表，判断链表中是否有环。
# 
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
# 
# 
# 
# 示例 1：
# 
# 输入：head = [3,2,0,-4], pos = 1
# 输出：true
# 解释：链表中有一个环，其尾部连接到第二个节点。
# 
# 
# 
# 
# 示例 2：
# 
# 输入：head = [1,2], pos = 0
# 输出：true
# 解释：链表中有一个环，其尾部连接到第一个节点。
# 
# 
# 
# 
# 示例 3：
# 
# 输入：head = [1], pos = -1
# 输出：false
# 解释：链表中没有环。
# 
# 
# 
# 
# 
# 
# 进阶：
# 
# 你能用 O(1)（即，常量）内存解决此问题吗？
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 思路1 : 用set保存地址，注意存的是listNode地址，而非val

# 思路2 ：快慢指针法
# 比较新奇。。。模拟快慢运动员赛跑，如果快的追上了慢的，就表明有环，在终点没路了就说明没环。这样不需要空间记录

class Solution:
    # def hasCycle(self, head: ListNode) -> bool:
    #     visited = set()
    #     while head:
    #         if head in visited:
    #             return True
    #         else:
    #             visited.add(head)
    #         head = head.next
        
    #     return False
        
    def hasCycle(self, head: ListNode) -> bool:
        if (head == None or head.next == None):
            return False
        slow = head
        fast = head.next
        while slow != fast:
            if (fast == None or fast.next == None):
                return False
            
            fast = fast.next.next
            slow = slow.next
        
        return True
        
# @lc code=end

