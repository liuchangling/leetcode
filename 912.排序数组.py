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
# 5. shell 5%
# 它是简单插入排序经过改进之后的一个更高效的版本，也称为缩小增量排序，同时该算法是冲破O(n2）的第一批算法之一。它与插入排序的不同之处在于，它会优先比较距离较远的元素。希尔排序又叫缩小增量排序。
# 希尔排序是把记录按下表的一定增量分组，对每组使用直接插入排序算法排序；随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。
# 原文链接：https://blog.csdn.net/weixin_41190227/article/details/86600821
#
# 6. 归并排序 30%
# 该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。
# 归并排序是一种稳定的排序方法。将已有序的子序列合并，得到完全有序的序列；
# 即先使每个子序列有序，再使子序列段间有序。
# 若将两个有序表合并成一个有序表，称为2-路归并。
# 合并的过程有点类似两个排序好的数组合并，之前写过类似代码
# 唯一的难点是递归的写法  merge(sort(left), sort(right))
# 其他代码蛮简单的

# 7 堆排序（Heapsort） 是指利用堆这种数据结构所设计的一种排序算法。
# 堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：
# 即子结点的键值或索引总是小于（或者大于）它的父节点。 
# 这个实现略复杂 这里不处理了

# 8 计数排序
# 使用场景为提前知道接结果范围。如果范围为k那么时间复杂度为o(n+k) 
# 核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。
# 作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数。
# 
# 步骤1：找出待排序的数组中最大和最小的元素；
# 步骤2：统计数组中每个值为i的元素出现的次数，存入数组C的第i项；
# 步骤3：对所有的计数累加（从C中的第一个元素开始，每一项和前一项相加）；
# 步骤4：反向填充目标数组：将每个元素i放在新数组的第C(i)项，每放一个元素就将C(i)减去1。

# 9 桶排序 是计数排序的升级版。它利用了函数的映射关系，高效与否的关键就在于这个映射函数的确定。
# 桶排序 (Bucket sort)的工作的原理：
# 假设输入数据服从均匀分布，将数据分到有限数量的桶里，每个桶再分别排序（有可能再使用别的排序算法或是以递归方式继续使用桶排序进行排

#  10 基数排序也是非比较的排序算法，对每一位进行排序，从最低位开始排序，复杂度为O(kn),为数组长度，k为数组中的数的最大的位数；

# 基数排序是按照低位先排序，然后收集；再按照高位排序，然后再收集；依次类推，直到最高位。有时候有些属性是有优先级顺序的，先按低优先级排序，再按高优先级排序。最后的次序就是高优先级高的在前，高优先级相同的低优先级高的在前。基数排序基于分别排序，分别收集，所以是稳定的。
# 步骤1：取得数组中的最大数，并取得位数；
# 步骤2：arr为原始数组，从最低位开始取每个位组成radix数组；
# 步骤3：对radix进行计数排序（利用计数排序适用于小范围数的特点）；
#  基数排序有两种方法：
# MSD 从高位开始进行排序
# LSD 从低位开始进行排序


# 基数排序 vs 计数排序 vs 桶排序
# 这三种排序算法都利用了桶的概念，但对桶的使用方法上有明显差异：
# 基数排序： 根据键值的每位数字来分配桶
# 计数排序： 每个桶只存储单一键值
# 桶排序： 每个桶存储一定范围的数值

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
    def sortArray(self, nums: List[int]) -> List[int]: 
        return self.quickSort(nums, 0, len(nums)-1)

    
    def quickSort(self, nums: List[int], low: int, high: int) -> List[int]:
        if low < high:
            index = self.partition(nums, low, high)
            self.quickSort(nums, low, index-1)
            self.quickSort(nums, index+1, high)
        return nums

   
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
    def partition(self, nums: List[int], low, high):
        index = low - 1 
        pivot = nums[high] 

        if low < high:
            for i in range(low, high):
                if nums[i] < pivot: 
                    index += 1
                    nums[i], nums[index] = nums[index], nums[i]
        index += 1
        nums[index], nums[high] = nums[high], nums[index]
        return index

    # shell排序 速度超越5%
    # 每个分组内用插入排序再合并
    # def sortArray(self, nums: List[int]) -> List[int]: 
    #     l = len(nums)
    #     gap = l >> 1
    #     while gap > 0 :
    #         for i in range(gap, l):
    #             temp = nums[i]
    #             preIndex = i - gap
    #             while preIndex >= 0 and nums[preIndex] > temp:
    #                 # 插入到合适位置
    #                 nums[preIndex + gap] = nums[preIndex]
    #                 preIndex -= gap
                
    #             nums[preIndex+gap]=temp
    #         gap = gap >> 1
    #     return nums

    # 归并排序 logn复杂度 最坏情况同样logn。但是需要额外空间
    # def sortArray(self, nums: List[int]) -> List[int]: 
    #     l = len(nums)
    #     if l == 1:
    #         return nums
    #     mid = len(nums) >> 1
    #     return self.merge(self.sortArray(nums[0:mid]),self.sortArray(nums[mid:l]))
    
    # def merge(self, a:List[int], b:List[int]) -> List[int]:
    #     c = [] 
    #     i = 0
    #     j = 0
    #     while i < len(a) and j < len(b):
    #         if a[i] < b[j]:
    #             c.append(a[i])
    #             i += 1
    #         else:
    #             c.append(b[j])
    #             j += 1
        
    #     if i < len(a):
    #         c = c + a[i:]
    #     if j < len(b):
    #         c = c + b[j:]
        
    #     return c
        



# @lc code=end