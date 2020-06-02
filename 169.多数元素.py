#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多数元素
#
# https://leetcode-cn.com/problems/majority-element/description/
#
# algorithms
# Easy (63.28%)
# Likes:    613
# Dislikes: 0
# Total Accepted:    171.6K
# Total Submissions: 270.8K
# Testcase Example:  '[3,2,3]'
#
# 给定一个大小为 n 的数组，找到其中的多数元素。多数元素是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。
# 
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
# 
# 
# 
# 示例 1:
# 
# 输入: [3,2,3]
# 输出: 3
# 
# 示例 2:
# 
# 输入: [2,2,1,1,1,2,2]
# 输出: 2
# 
# 
# 第一反应就是hash表计算，优化的话可以当统计到n/2就返回。 时间复杂度o(n) 空间复杂度o(n)


#  高级： Boyer-Moore 投票算法
# 思路

# 如果我们把众数记为 +1+1，把其他数记为 -1−1，将它们全部加起来，显然和大于 0，从结果本身我们可以看出众数比其他数多。

# 算法

# Boyer-Moore 算法的本质和方法四中的分治十分类似。我们首先给出 Boyer-Moore 算法的详细步骤：

# 我们维护一个候选众数 candidate 和它出现的次数 count。初始时 candidate 可以为任意值，count 为 0；

# 我们遍历数组 nums 中的所有元素，对于每个元素 x，在判断 x 之前，如果 count 的值为 0，我们先将 x 的值赋予 candidate，随后我们判断 x：

# 如果 x 与 candidate 相等，那么计数器 count 的值增加 1；

# 如果 x 与 candidate 不等，那么计数器 count 的值减少 1。

# 在遍历完成后，candidate 即为整个数组的众数。


# @lc code=start
import collections
class Solution:
    # def majorityElement(self, nums: List[int]) -> int:
    #     counts = collections.Counter(nums)
    #     return max(counts.keys(), key=counts.get)
    
    def majorityElement(self, nums: List[int]) -> int:
        count = 0 
        for n in nums:
            if count == 0 :
                candidate = n

            if candidate == n :
                count += 1
            else:
                count -= 1

        
        return candidate
    
# @lc code=end

