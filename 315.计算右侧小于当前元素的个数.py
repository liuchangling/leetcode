#
# @lc app=leetcode.cn id=315 lang=python3
#
# [315] 计算右侧小于当前元素的个数
#
# https://leetcode-cn.com/problems/count-of-smaller-numbers-after-self/description/
#
# algorithms
# Hard (37.84%)
# Likes:    326
# Dislikes: 0
# Total Accepted:    25.1K
# Total Submissions: 64.3K
# Testcase Example:  '[5,2,6,1]'
#
# 给定一个整数数组 nums，按要求返回一个新数组 counts。数组 counts 有该性质： counts[i] 的值是  nums[i] 右侧小于
# nums[i] 的元素的数量。
# 
# 示例:
# 
# 输入: [5,2,6,1]
# 输出: [2,1,1,0] 
# 解释:
# 5 的右侧有 2 个更小的元素 (2 和 1).
# 2 的右侧仅有 1 个更小的元素 (1).
# 6 的右侧有 1 个更小的元素 (1).
# 1 的右侧有 0 个更小的元素.
# 
# 
# 逆序遍历， 遇到一个值更新遇到的count map. 
# tle了。。。 时间复杂度是O(n2)

from collections import defaultdict

# @lc code=start
class Solution:
    # TLE
    # def countSmaller(self, nums: List[int]) -> List[int]:
    #     m = defaultdict(int)
    #     ans = [0 for _ in range(len(nums))]

    #     for i in range(len(nums)-1, -1 , -1):
    #         cur = nums[i]
    #         count = 0 
    #         for key in m:
    #             if key < cur: count += m[key]
            
    #         ans[i] = count
    #         m[cur] = m[cur] + 1
        

    #     return ans
    

    def countSmaller(self, nums: List[int]) -> List[int]:
        m = defaultdict(int)
        ans = [0 for _ in range(len(nums))]

        for i in range(len(nums)-1, -1 , -1):
            cur = nums[i]
            count = 0 
            for n in nums[i+1:]:
                if n < cur: count += 1

            ans[i] = count        

        return ans


        
# @lc code=end

