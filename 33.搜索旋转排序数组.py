#
# @lc app=leetcode.cn id=33 lang=python3
#
# [33] 搜索旋转排序数组
#
# https://leetcode-cn.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (36.44%)
# Likes:    721
# Dislikes: 0
# Total Accepted:    120.1K
# Total Submissions: 317.4K
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
# 
# ( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。
# 
# 搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。
# 
# 你可以假设数组中不存在重复的元素。
# 
# 你的算法时间复杂度必须是 O(log n) 级别。
# 
# 示例 1:
# 
# 输入: nums = [4,5,6,7,0,1,2], target = 0
# 输出: 4
# 
# 
# 示例 2:
# 
# 输入: nums = [4,5,6,7,0,1,2], target = 3
# 输出: -1
# 
# 思路1 好奇.index是否会TLE 。。 测试结果超74% 没有TLE
# 思路2 修改二分查找的区域，因为每次切分，至少有一半为有序，判断是否target在该区间，如否则找另一半。
#                    target > nums[mid]      target < nums[mid]
# 左有序（左边都是原来右边)   右                       都可能
# 右有序（右边都是原来左边)   都可能                     左
# 测试结果性能超97%
# from typing import List
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # return nums.index(target) if (target in nums) else -1

        l = 0
        h = len(nums) - 1

        while l <= h :
            mid = (l + h) // 2

            x = nums[mid]
            if target == x:
                return mid
            elif target < x: 
                if nums[l] <= x:
                    # 左有序
                    if nums[l] == target:
                        return l
                    elif nums[l] < target:
                        h = mid - 1
                    else:
                        l = mid + 1                
                else:
                    # 右有序
                    h = mid - 1
            else :
                # target > x
                if nums[l] <= x:
                    # 左有序
                    l = mid + 1
                else:
                    # 右有序
                    if nums[h] == target:
                        return h
                    elif nums[h] > target:
                        l = mid + 1
                    else :
                        h = mid - 1
        
        return -1

# @lc code=end


# print(Solution().search([3,1], 1))