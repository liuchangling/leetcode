#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#
# https://leetcode-cn.com/problems/subsets/description/
#
# algorithms
# Medium (77.27%)
# Likes:    590
# Dislikes: 0
# Total Accepted:    94.4K
# Total Submissions: 122.1K
# Testcase Example:  '[1,2,3]'
#
# 给定一组不含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 
# 说明：解集不能包含重复的子集。
# 
# 示例:
# 
# 输入: nums = [1,2,3]
# 输出:
# [
# ⁠ [3],
# [1],
# [2],
# [1,2,3],
# [1,3],
# [2,3],
# [1,2],
# []
# ]
# 
#

# 思路1 递归 先在ans放入[]。 每遍历到一个数，将ans中所有答案加上当前数，然后插入ans中 70%

# 思路2 回溯
# 定义一个回溯方法 backtrack(first, curr)，第一个参数为索引 first，第二个参数为当前子集 curr。
# 如果当前子集构造完成，将它添加到输出集合中。
# 否则，从 first 到 n 遍历索引 i。
# 将整数 nums[i] 添加到当前子集 curr。
# 继续向子集中添加整数：backtrack(i + 1, curr)。
# 从 curr 中删除 nums[i] 进行回溯。


#  回溯算法实现框架

# ans = []
# def backtrack(path, choices):
#     if path is valid:
#         ans.append(path)
#         return 
    
#     for choice in choices:
#         makeChoice(choice) # 通常会更新path和choices

#         backtrack(path, choices)

#         revertChoice(choice) # 撤销刚才的更新


# 思路3 转换为n位2进制处理
# 0表示无，1表示有 该方法思路来自于 Donald E. Knuth。据说是最快的，可能因为测试用例少，所以没体现出来。
# 转化二进制代码：
# nth_bit = 1 << n
# for i in range(2**n):
#     # generate bitmask, from 0..00 to 1..11
#     bitmask = bin(i | nth_bit)[3:]

# 或者简单低效的方式：
# for i in range(2**n, 2**(n + 1)):
#     # generate bitmask, from 0..00 to 1..11
#     bitmask = bin(i)[3:]

# 这里的[3:] 是为了去掉'0bxxxxx'前面的0b直接得到xxxxx


from typing import List

# @lc code=start
class Solution:
    # 思路1  98%
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     ans = [[]]
    #     for n in nums:
    #         tmp = []
    #         for j in ans:
    #             tmp.append( j + [n] )
            
    #         ans += tmp

    #     return ans

    # 代码简化后 98%
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]

        for n in nums:
          ans += [ cur + [n] for cur in ans]

        return ans

    # 标准回溯写法为 87%
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     L = len(nums)
    #     if L == 0: return []

    #     ans = []

    #     def backtrack(doneIndex, toDoList):
    #         ans.append(toDoList[:])

    #         for i in range(doneIndex, L):
    #             toDoList.append(nums[i])
    #             backtrack(i + 1, toDoList)
    #             toDoList.pop() # backtrack


    #     backtrack(0, [])

    #     return ans

    # 简化后回溯 87%
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     L = len(nums)
    #     if L == 0: return []

    #     ans = []

    #     def backtrack(doneIndex, toDoList):
    #         ans.append(toDoList)

    #         for i in range(doneIndex, L):
    #             backtrack(i + 1, toDoList+[nums[i]])

    #     backtrack(0, [])

    #     return ans

    # 思路3  二进制 70%
    # def subsets(self, nums: List[int]) -> List[List[int]]:
    #     L = len(nums)
    #     ans = []
    #     for i in range(2**L, 2**(L+1)):
    #         bit = bin(i)[3:]
            
    #         ans.append([nums[j]  for j in range(L) if bit[j]=='1'])
    #     return ans
            

# @lc code=end

# print(Solution().subsets([1,2,3]))
