#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#
# https://leetcode-cn.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Hard (49.02%)
# Likes:    370
# Dislikes: 0
# Total Accepted:    46.7K
# Total Submissions: 94.1K
# Testcase Example:  '[100,4,200,1,3,2]'
#
# 给定一个未排序的整数数组，找出最长连续序列的长度。
# 
# 要求算法的时间复杂度为 O(n)。
# 
# 示例:
# 
# 输入: [100, 4, 200, 1, 3, 2]
# 输出: 4
# 解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
# 

# 想法1 sort 然后遍历   O(nlgn)

# 想法2 错误 题目要求O(n) 那肯定要用空间来换，我想着先创建一个bool数组，然后遍历这个数组,时间复杂度是O(n)。
# 不过这个bool数组长度是数组最大值. 这是一个错误的想法。因为数组有负数，那么额外的数组空间不行，考虑换成别的数据结构

# 思路1 先用集合进行去重，因为n-1不在集合中才表示n是一个起点，我们只需要对这样的数检查 n+1 n+2..到哪停止，并更新ans即可。 99%

# @lc code=start    


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ans = 0

        for n in s :
            # 如果无前驱才计算count
            if n-1 not in s :
                count = 1

                i = n + 1

                while i in s:
                    count += 1
                    i += 1
                
                ans = max(count, ans)
        
        return ans
            


# @lc code=end

