#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#
# https://leetcode-cn.com/problems/permutations/description/
#
# algorithms
# Medium (76.05%)
# Likes:    713
# Dislikes: 0
# Total Accepted:    130.3K
# Total Submissions: 171.4K
# Testcase Example:  '[1,2,3]'
#
# 给定一个 没有重复 数字的序列，返回其所有可能的全排列。
# 
# 示例:
# 
# 输入: [1,2,3]
# 输出:
# [
# ⁠ [1,2,3],
# ⁠ [1,3,2],
# ⁠ [2,1,3],
# ⁠ [2,3,1],
# ⁠ [3,1,2],
# ⁠ [3,2,1]
# ]
# 
# dfs + 回溯算法 + 递归 很高级的思想，代码很简单
# 时间复杂度为 O(n * n!)O(n∗n!)
# 空间复杂度：O(n)



# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        first = 0 
        res = []
        size = len(nums)

        def back_track(first):
            if first == size :
                res.append(nums[:])
            
            for i in range(first, size):
                # 0~first为已使用， first~size-1为未使用
                # 动态维护数组
                nums[i] , nums[first] = nums[first], nums[i]
                # 继续递归填下一个数
                back_track(first + 1)
                # 撤销操作
                nums[i] , nums[first] = nums[first], nums[i]

        back_track(first)
        return res


# @lc code=end

