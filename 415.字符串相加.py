#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] 字符串相加
#
# https://leetcode-cn.com/problems/add-strings/description/
#
# algorithms
# Easy (49.58%)
# Likes:    159
# Dislikes: 0
# Total Accepted:    33.5K
# Total Submissions: 67.1K
# Testcase Example:  '"0"\n"0"'
#
# 给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。
# 
# 注意：
# 
# 
# num1 和num2 的长度都小于 5100.
# num1 和num2 都只包含数字 0-9.
# num1 和num2 都不包含任何前导零。
# 你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
# 
# 
# 用一个借位完成， 需要注意一下 1 9这个测试用例，last会成为新的一位


# @lc code=start
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        last = 0 
        r1 = len(num1) - 1
        r2 = len(num2) - 1
        ans = ''

        while r1 >= 0 or r2 >= 0 or last == 1 :
            n1 = int(num1[r1]) if r1>=0 else 0
            n2 = int(num2[r2]) if r2>=0 else 0
            t = n1 + n2 + last
            ans = str(t % 10) + ans
            last = t // 10
            r1 -= 1
            r2 -= 1

        return  ans
        
# @lc code=end

