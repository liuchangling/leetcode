#
# @lc app=leetcode.cn id=88 lang=python3
#
# [88] 合并两个有序数组
#
# https://leetcode-cn.com/problems/merge-sorted-array/description/
#
# algorithms
# Easy (45.68%)
# Likes:    424
# Dislikes: 0
# Total Accepted:    110.3K
# Total Submissions: 236.3K
# Testcase Example:  '[1,2,3,0,0,0]\n3\n[2,5,6]\n3'
#
# 给定两个有序整数数组 nums1 和 nums2，将 nums2 合并到 nums1 中，使得 num1 成为一个有序数组。
# 
# 说明:
# 
# 
# 初始化 nums1 和 nums2 的元素数量分别为 m 和 n。
# 你可以假设 nums1 有足够的空间（空间大小大于或等于 m + n）来保存 nums2 中的元素。
# 
# 
# 示例:
# 
# 输入:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3
# 
# 输出: [1,2,2,3,5,6]
# 
# 思路1 这道题借用额外空间就很像那个两个有序链表的合并
# 思路2 如果想额外空间为O(1) 我们需要让指针从后向前遍历
# 
# 代码优化，使用切片完成最后一步拷贝数组 不过两者都是8%的速度。。。很神奇啊最近咋都这么慢
# 思路3  合并后排序  理论上时间复杂度是O(nlgn) 会大于前两种

# @lc code=start
class Solution:
    # 思路2
    # def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    #     """
    #     Do not return anything, modify nums1 in-place instead.
    #     """
        
    #     p = m + n - 1
    #     p1 = m - 1
    #     p2 = n - 1

    #     while p >= 0:
    #         if p1 == -1:
    #             nums1[p] = nums2[p2]
    #             p2 -= 1
    #         elif p2 == -1:
    #             return nums1
    #         elif nums1[p1] < nums2[p2] :
    #             nums1[p] = nums2[p2]
    #             p2 -= 1
    #         else :
    #             nums1[p] = nums1[p1]
    #             p1 -= 1
    #         p -= 1

    #     return nums1           

    # 思路2 优化
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p = m + n - 1
        p1 = m - 1
        p2 = n - 1

        while p1 >= 0 and p2 >= 0 :
            if nums1[p1] < nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
            else:
                nums1[p] = nums1[p1]
                p1 -= 1
            p -= 1
        
        # 挺秀的
        # add missing elements from nums2
        nums1[ : p2 + 1] = nums2[ : p2 + 1]

        return nums1

    # 思路3 排序
    # def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:    
    #     nums1[m:] = nums2
    #     nums1.sort()
    #     return nums1
            
# @lc code=end

