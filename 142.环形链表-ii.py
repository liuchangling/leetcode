#
# @lc app=leetcode.cn id=142 lang=python3
#
# [142] 环形链表 II
#
# https://leetcode-cn.com/problems/linked-list-cycle-ii/description/
#
# algorithms
# Medium (50.29%)
# Likes:    502
# Dislikes: 0
# Total Accepted:    83K
# Total Submissions: 164.3K
# Testcase Example:  '[3,2,0,-4]\n1'
#
# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
# 
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。
# 
# 说明：不允许修改给定的链表。
# 
# 
# 
# 示例 1：
# 
# 输入：head = [3,2,0,-4], pos = 1
# 输出：tail connects to node index 1
# 解释：链表中有一个环，其尾部连接到第二个节点。
# 
# 
# 
# 
# 示例 2：
# 
# 输入：head = [1,2], pos = 0
# 输出：tail connects to node index 0
# 解释：链表中有一个环，其尾部连接到第一个节点。
# 
# 
# 
# 
# 示例 3：
# 
# 输入：head = [1], pos = -1
# 输出：no cycle
# 解释：链表中没有环。
# 
# 
# 
# 
# 
# 
# 进阶：
# 你是否可以不用额外空间解决此题？
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 141题 升级版
# 思路1 借助set的O(n)额外空间的实现没有区别
# 思路2 Floyd 算法 
#       快慢指针有区别。官方题解有一个证明。有图示，可以去看看https://leetcode-cn.com/problems/linked-list-cycle-ii/solution/huan-xing-lian-biao-ii-by-leetcode/
#       在141中，我们只要快慢指针相遇，就返回就行了，这题要返回入口，在相遇之后我们令指针a从head开始，指针b从相遇位置开始，每次移动一格，直到相遇，
#       相遇位置就是入口位置。

# 证明如下：
# 2⋅distance(tortoise)=distance(hare)
# 2(F+a)=F+a+b+a
# 2F+2a=F+2a+b
# F=b

# @lc code=start
class Solution:
    # 思路1 用集合， 91% 借助了额外空间
    # def detectCycle(self, head: ListNode) -> ListNode:
    #     visited = set()
    #     while head:
    #         if head in visited:
    #             return head
    #         else:
    #             visited.add(head)
    #         head = head.next
        
    #     return None

    # 思路2  Floyd 算法 65% 无需额外空间
    def detectCycle(self, head: ListNode) -> ListNode:
        slow, fast = head, head
        
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast : break

        if fast is None or fast.next is None:
            return None
            
        # now slow and fast get intersect
        fast = head

        while fast != slow:
            fast = fast.next
            slow = slow.next

        return slow

        
# @lc code=end

