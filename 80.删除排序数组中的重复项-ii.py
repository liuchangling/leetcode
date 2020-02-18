#
# @lc app=leetcode.cn id=80 lang=python3
#
# [80] 删除排序数组中的重复项 II
# 
# 使用一个指针和一个计数器
# 遍历时如果和之前的数相同则计数器加一，不同则重制为1
# 然后计数器在1-2则记录数字，指针加一，超过2则丢弃，不做操作


from typing import List
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lastIndex = 1
        count = 1
        for i in range(1,len(nums)):
            if nums[i] == nums[i-1]:
                count += 1
            else:
                count = 1
        
            if count <= 2:
                nums[lastIndex] = nums[i]
                lastIndex += 1
        
        return lastIndex
        
# @lc code=end

