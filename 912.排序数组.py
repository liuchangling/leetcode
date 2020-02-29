#
# @lc app=leetcode.cn id=912 lang=python3
#
# [912] 排序数组
#
# https://leetcode-cn.com/problems/sort-an-array/description/
#
# algorithms
# Medium (51.42%)
# Likes:    46
# Dislikes: 0
# Total Accepted:    15.9K
# Total Submissions: 30.2K
# Testcase Example:  '[5,2,3,1]'
#
# 给定一个整数数组 nums，将该数组升序排列。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 
# 输入：[5,2,3,1]
# 输出：[1,2,3,5]
# 
# 
# 示例 2：
# 
# 
# 输入：[5,1,1,2,0,0]
# 输出：[0,0,1,1,2,5]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length <= 10000
# -50000 <= A[i] <= 50000
# 
# 没什么好解释的 你懂得 
# 1. 冒泡 超时
# 重复地走访过要排序的数列，一次比较两个元素，如果它们的顺序错误就把它们交换过来。

# 2. 选择 超时
# 首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
# 然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。

# 3. 插入 超时
# 通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。

# 4. 快速 随机 46% 固定 73%
# 通过一趟排序将待排记录分隔成独立的两部分，其中一部分记录的关键字均比另一部分的关键字小，
# 则可分别对这两部分记录继续进行排序，以达到整个序列有序。
# 步骤1：从数列中挑出一个元素，称为 “基准”（pivot ）；
# 步骤2：重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
# 步骤3：递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
# 分区操作有点秀。可以pivot用low，记录临时index = low-1，  每当找到一个小于pivot的值，就index++并交换找到的较小值与index的元素，最终pivot放在index上即可
#
# 5. shell
# 它是简单插入排序经过改进之后的一个更高效的版本，也称为缩小增量排序，同时该算法是冲破O(n2）的第一批算法之一。它与插入排序的不同之处在于，它会优先比较距离较远的元素。希尔排序又叫缩小增量排序。
# 希尔排序是把记录按下表的一定增量分组，对每组使用直接插入排序算法排序；随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。
# 原文链接：https://blog.csdn.net/weixin_41190227/article/details/86600821


from typing import List
# import random
# @lc code=start
class Solution:
    # 冒泡  会超时 优化思路：记录上一次交换位置后续不用再移动
    # def sortArray(self, nums: List[int]) -> List[int]:        
    #     length = len(nums)
    #     for i in range(length - 1):
    #         for j in range(0, length - i - 1):
    #             if nums[j] > nums[j+1]:
    #                 t = nums[j]
    #                 nums[j] = nums[j+1]
    #                 nums[j+1] = t

    #     return nums

    # 选择排序，每次找到最小的，和当前节点交换 寻找[i, n)区间里的最小值的索引
    # def sortArray(self, nums: List[int]) -> List[int]: 
    #     length = len(nums)
    #     for i in range(length - 1):
    #         m = nums[i]
    #         temp = i 
    #         for j in range(i + 1, length):
    #             if m > nums[j] :
    #                 temp = j 
    #                 m = nums[j]

    #         nums[temp] = nums[i]
    #         nums[i] = m
        
    #     return nums

    # 插入排序， 每次插到前面数组中合适的位置
    # def sortArray(self, nums: List[int]) -> List[int]: 
    #     length = len(nums)
    #     for i in range(1, length):
    #         t = nums[i]
    #         temp = 0
    #         for j in reversed(range(0, i)):
    #             if nums[j] > t :
    #                 nums[j+1] = nums[j]
    #             else :
    #                 temp = j + 1
    #                 break
            
    #         nums[temp] = t

    #     return nums



    # 插入排序
    # def sortArray(self, nums: List[int]) -> List[int]: 
    #     for i in range(1, len(nums)):
    #         j = i
    #         while nums[j] < nums[j-1] and j > 0:
    #             nums[j], nums[j-1] = nums[j-1], nums[j]
    #             j -= 1
    #     return nums
            

    # 快速排序
    # def sortArray(self, nums: List[int]) -> List[int]: 
    #     return self.quickSort(nums, 0, len(nums)-1)

    
    # def quickSort(self, nums: List[int], low: int, high: int) -> List[int]:
    #     if low < high:
    #         index = self.partition(nums, low, high)
    #         self.quickSort(nums, low, index-1)
    #         self.quickSort(nums, index+1, high)
    #     return nums

   
    # 分治法思想，体现在分区，返回index，再对于index左右两边进行递归排序

    # pivot下标随机 击败44%
    # def partition(self, nums: List[int], low, high):
    #     index = low - 1 #这是一个很巧妙的代码，从小于low的位置开始走起。把low到high-1顺序遍历一次即可
    #     rint = random.randint(low, high)# 随机取一个pivot 
    #     pivot = nums[rint] # 因为不会遍历到high的元素，有些写法直接使用nums[high] ，可读性较差,写一个pivot会清晰一点

    #     nums[rint], nums[high] = nums[high], nums[rint]

    #     if low < high:
    #         for i in range(low, high):
    #             if nums[i] < pivot: # 当前访问元素小于pivot时                    
    #                 # 再将上一次index +1 的位置和当前元素对调，注意这里可以先进行index++操作
    #                 index += 1
    #                 nums[i], nums[index] = nums[index], nums[i]
    #     # 到此位置 index的位置左侧都是小于pivot的        
    #     index += 1
    #     nums[index] , nums[high] = nums[high], nums[index]
    #     return index

    # pivot index选取使用固定值 击败44%
    # def partition(self, nums: List[int], low, high):
    #     index = low - 1 
    #     pivot = nums[high] 

    #     if low < high:
    #         for i in range(low, high):
    #             if nums[i] < pivot: 
    #                 index += 1
    #                 nums[i], nums[index] = nums[index], nums[i]
    #     index += 1
    #     nums[index], nums[high] = nums[high], nums[index]
    #     return index

    # shell排序
    # 每个分组内用插入排序再合并
    def sortArray(self, nums: List[int]) -> List[int]: 
        gap = len(nums) >> 1
        while gap > 0 :
            



# @lc code=end