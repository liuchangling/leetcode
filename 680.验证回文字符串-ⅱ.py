#
# @lc app=leetcode.cn id=680 lang=python3
#
# [680] 验证回文字符串 Ⅱ
#
# https://leetcode-cn.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (35.58%)
# Likes:    167
# Dislikes: 0
# Total Accepted:    27.4K
# Total Submissions: 71.2K
# Testcase Example:  '"aba"'
#
# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
# 
# 示例 1:
# 
# 
# 输入: "aba"
# 输出: True
# 
# 
# 示例 2:
# 
# 
# 输入: "abca"
# 输出: True
# 解释: 你可以删除c字符。
# 
# 
# 注意:
# 
# 
# 字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。
# 
# 思路1 左右指针就是遍历，然后遇到不匹配的情况分为跳过左边和跳过右边去算
# 思路2 可以代码可以更简化一点

# @lc code=start
class Solution:
    # def validPalindrome(self, s: str) -> bool:
    #     l = 0
    #     r = len(s) - 1

    #     while l < r:
    #         if s[l] == s[r]:
    #             l += 1
    #             r -= 1
    #         else:
    #             break 

    #     if l >= r:
    #         return True

    #     l1 = l+1
    #     r1 = r 
    #     while l1 < r1:
    #         if s[l1] == s[r1]:
    #             l1 += 1
    #             r1 -= 1
    #         else:
    #             break

    #     if l1 >= r1:
    #         return True

    #     l2 = l
    #     r2 = r-1
    #     while l2 < r2:
    #         if s[l2] == s[r2]:
    #             l2 += 1
    #             r2 -= 1
    #         else:
    #             return False

    #     return True

    def validPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                s1 = s[l+1:r+1]
                s2 = s[l:r] 
                return s1 == s1[::-1] or s2 == s2[::-1] 

        return True
        

        
# @lc code=end

