#
# @lc app=leetcode.cn id=984 lang=python3
#
# [984] 不含 AAA 或 BBB 的字符串
#
# https://leetcode-cn.com/problems/string-without-aaa-or-bbb/description/
#
# algorithms
# Medium (36.04%)
# Likes:    45
# Dislikes: 0
# Total Accepted:    4.2K
# Total Submissions: 11.4K
# Testcase Example:  '1\n2'
#
# 给定两个整数 A 和 B，返回任意字符串 S，要求满足：
# 
# 
# S 的长度为 A + B，且正好包含 A 个 'a' 字母与 B 个 'b' 字母；
# 子串 'aaa' 没有出现在 S 中；
# 子串 'bbb' 没有出现在 S 中。
# 
# 
# 
# 
# 示例 1：
# 
# 输入：A = 1, B = 2
# 输出："abb"
# 解释："abb", "bab" 和 "bba" 都是正确答案。
# 
# 
# 示例 2：
# 
# 输入：A = 4, B = 1
# 输出："aabaa"
# 
# 
# 
# 提示：
# 
# 
# 0 <= A <= 100
# 0 <= B <= 100
# 对于给定的 A 和 B，保证存在满足要求的 S。
# 
# 情况1 AB相等时直接return
# 情况2 直接创建一个较多a或者较多b的字符串，转成list后就地修改。
# 大多数情况直接插入在3*i-1的位置即可。比较繁琐的情况可能会数组越界。

# 令 total = A+B
# 当 total 不能被3整除的情况，直接插入在 （3*i -1）% total的位置即可
# 比较繁琐的是 total 能被3整除的情况， 这样的case需要特殊处理为3 * i - 2 - total。
# 速度超越95%

# @lc code=start
class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        if A==B:
            return 'ab'*A
        
        if A>B:
            more = 'a'
            less = 'b'
            times = B
        else :
            more = 'b'
            less = 'a'
            times = A

        total = A+B
        l = list (more * total)

        i = 1
        while i <= times:
            l[(3 * i - 1) % total] = less

            if 3 * i - 1 >= total and total % 3 == 0:
                l[3 * i - 2 - total] = less
            i += 1
     
        return ''.join(l)

        
# @lc code=end

