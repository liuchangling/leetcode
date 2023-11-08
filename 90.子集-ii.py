#
# @lc app=leetcode.cn id=90 lang=python3
#
# [90] 子集 II
#
# https://leetcode-cn.com/problems/subsets-ii/description/
#
# algorithms
# Medium (59.99%)
# Likes:    235
# Dislikes: 0
# Total Accepted:    35.2K
# Total Submissions: 58.6K
# Testcase Example:  '[1,2,2]'
#
# 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
# 
# 说明：解集不能包含重复的子集。
# 
# 示例:
# 
# 输入: [1,2,2]
# 输出:
# [
# ⁠ [2],
# ⁠ [1],
# ⁠ [1,2,2],
# ⁠ [2,2],
# ⁠ [1,2],
# ⁠ []
# ]
# 类似 78题
# 思路1 回溯
# 先排序，然后对回溯算法修改，有一定条件是不做任何选择，直接跳到下一项的
#
# 思路2 迭代
# 78题的迭代写起来特别爽，这个倒不是很爽。。
# 区别就一个，如果出现了相同的解，那么新的解只在上一次出现的解后面加新的数
# 而非全部解中加新的数

# from typing import List
# from collections import defaultdict
# @lc code=start
class Solution:
    # 思路1 93%
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:      
        L = len(nums)
        if L == 0: return []
        
        nums.sort()
        ans = []
        
        def backtrack(doneIndex, toDoList):
            ans.append(toDoList)

            for i in range(doneIndex, L):
                # 当这次要添加的选择是重复的，就跳过
                if i > doneIndex and nums[i] == nums[i-1]: continue

                backtrack(i + 1, toDoList+[nums[i]])

        backtrack(0, [])

        return ans

    # 思路2 64%
    # def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    #     ans, cur = [[]], []
    #     nums.sort()

    #     for i in range(len(nums)):
    #         if i > 0 and nums[i] == nums[i-1]:
    #             # 连续2相同, cur为上一次添加进来的解
    #             cur = [tmp + [nums[i]] for tmp in cur]
    #         else :
    #             # 新的数
    #             cur = [tmp + [nums[i]] for tmp in ans]

    #         ans += cur

    #     return ans


# @lc code=end

# print(Solution().subsetsWithDup([1,2,2]))


# /**
#  * @param {number[]} nums
#  * @return {number[][]}
#  */

# var subsetsWithDup = function(nums) {    
#     nums.sort() // 90题先排序可以去掉一些遍历
#     let ret = []
#     function back_track(path, choices){

#         // if valid, add path to result
#         ret.push(path)

#         // search all choices
#         choices.forEach((choice, index) => {

#             // 90题需要的防重处理
#             if(index>0 && choice === choices[index -1]){
#                 return                
#             }
         
#             // make 1 choice . remove this choice
#             // 全排列 
#             // let temp = choices.slice(0, index).concat(choices.slice(index+1))
#             // 不重复子集
#             let temp = choices.slice(index+1)

#             // update path
#             let makeChoice = path.concat([choice])
          
        
#             // backtrack after make choice
#             back_track(makeChoice, temp)
#             // revert choice
#             // 回退 js的concat不修改原数组，所以这一步不用写了            
#         });
#     }

#     back_track([], nums)
#     return ret
# };

