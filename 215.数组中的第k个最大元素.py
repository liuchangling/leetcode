#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#
# https://leetcode-cn.com/problems/kth-largest-element-in-an-array/description/
#
# algorithms
# Medium (59.00%)
# Likes:    371
# Dislikes: 0
# Total Accepted:    78.5K
# Total Submissions: 128.5K
# Testcase Example:  '[3,2,1,5,6,4]\n2'
#
# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
# 
# 示例 1:
# 
# 输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
# 
# 
# 示例 2:
# 
# 输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4
# 
# 说明: 
# 
# 你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。
# 
# k = 1 的情况 很明显时间复杂度为o(n)
# 

from typing import List
import random

# @lc code=start
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def part(left: int, right: int, pivot_index: int):
            pivot = nums[pivot_index]
            nums[right], nums[pivot_index] = nums[pivot_index], nums[right]
            low = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[low] , nums[i] = nums[i], nums[low]
                    low += 1
            nums[right], nums[low] = nums[low], nums[right]
            return low

        def select(left: int, right:int, target:int):
            if left == right:
                return nums[left]

            # 也可以随机选取 pivot_index = left
            pivot_index = random.randint(left, right)
            
            pivot_index = part(left, right, pivot_index)
            
            if target == pivot_index:
                return nums[pivot_index]
            elif target < pivot_index:
                return select(left, pivot_index-1, target)
            else:
                return select(pivot_index+1, right, target)
        
        
        return select(0, len(nums)-1, len(nums) - k)

# @lc code=end

