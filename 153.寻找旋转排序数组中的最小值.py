#
# @lc app=leetcode.cn id=153 lang=python3
#
# [153] 寻找旋转排序数组中的最小值
#
# https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array/description/
#
# algorithms
# Medium (50.25%)
# Likes:    180
# Dislikes: 0
# Total Accepted:    47K
# Total Submissions: 92.7K
# Testcase Example:  '[3,4,5,1,2]'
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# 
# ( 例如，数组 [0,1,2,4,5,6,7]  可能变为 [4,5,6,7,0,1,2] )。
# 
# 请找出其中最小的元素。
# 
# 你可以假设数组中不存在重复元素。
# 
# 示例 1:
# 
# 输入: [3,4,5,1,2]
# 输出: 1
# 
# 示例 2:
# 
# 输入: [4,5,6,7,0,1,2]
# 输出: 0
# 
# 1. return min(nums) 超越88%。。。看来这么搞得人蛮多的
# 2. 旋转前就是0号位，说白了就找到i满足 nums[i-1]>nums[i]。
#    一顿操作猛如虎，然后超越了51%。。。
# 3. 根据有序的情况进行返回，优化代码逻辑后超越了88%。貌似和方案1差不多
# 4. 大佬从右侧先判断，进行缩减区域，超越了96%

# from typing import List
# @lc code=start
class Solution:
    # def findMin(self, nums: List[int]) -> int:

    #     l = 0
    #     h = len(nums) - 1

    #     while l <= h :

    #         mid = (l + h) // 2
    #         x = nums[mid]

    #         if l + 2 >= h:
    #             return min(nums[l], x, nums[h])

    #         if x < nums[mid - 1]:
    #             return x
            
    #         if x > nums[mid + 1]:
    #             return nums[mid + 1]

    #         if nums[l] <= x <= nums[h]:
    #             return nums[l]
    #         elif nums[h] < x:
    #             l = mid + 1
    #         else :
    #             h = mid - 1
    
    # def findMin(self, nums: List[int]) -> int:
    #     l = 0
    #     h = len(nums) - 1
    #     while l <= h :
    #         mid = (l + h) // 2
    #         x = nums[mid]

    #         if nums[l] > x:
    #             # 仅右有序
    #             h = mid - 1
    #             if nums[h] > x:
    #                 # x满足条件即返回
    #                 return x
    #         elif x <= nums[h]: 
    #             # 全有序
    #             return nums[l]
    #         else :
    #             # 仅左有序
    #             l = mid + 1
    
     def findMin(self, nums: List[int]) -> int:
        l = 0
        h = len(nums) - 1
        while l < h :
            mid = (l + h) // 2
            x = nums[mid]

            if nums[h] < x:
                # 仅左有序
                l = mid + 1
            else :
                h = mid
            
        return nums[l]

# @lc code=end
# Solution().findMin([1])
