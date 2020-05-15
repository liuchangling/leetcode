#
# @lc app=leetcode.cn id=560 lang=python3
#
# [560] 和为K的子数组
#
# https://leetcode-cn.com/problems/subarray-sum-equals-k/description/
#
# algorithms
# Medium (43.99%)
# Likes:    350
# Dislikes: 0
# Total Accepted:    33.4K
# Total Submissions: 75.2K
# Testcase Example:  '[1,1,1]\n2'
#
# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
# 
# 示例 1 :
# 
# 
# 输入:nums = [1,1,1], k = 2
# 输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
# 
# 
# 说明 :
# 
# 
# 数组的长度为 [1, 20,000]。
# 数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。
# 
# 
# 暴力法就不写了 TLE
# 思路1： 前缀和
#      从左到右遍历一次，计算pre。
#      对于第j个元素， 我们需要找前面有多少个pre[i] 值为 k - pre[j] 
#      会TLE
# 思路2： 对于思路1进行优化，
#        将pre数组优化为一个统计出现次数的map

# @lc code=start
class Solution:
    # def subarraySum(self, nums: List[int], k: int) -> int:
    #     pre = [0]
    #     count = 0
    #     for n in nums:
    #         sum = n + pre[-1]
    #         target = sum - k
            
    #         for p in pre:
    #             if p == target:
    #                 count +=1
    #         pre.append( sum )
        
    #     return count
        
    def subarraySum(self, nums: List[int], k: int) -> int:
        m = {0:1}
        count = 0
        pre = 0

        for n in nums:
            pre = n + pre
            target = pre - k

            if target in m:
                count += m[target]

            if pre in m:
                m[pre] = m[pre] + 1
            else :
                m[pre] = 1
        
        return count

# @lc code=end

