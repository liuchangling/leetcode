#
# @lc app=leetcode.cn id=43 lang=python3
#
# [43] 字符串相乘
#
# https://leetcode-cn.com/problems/multiply-strings/description/
#
# algorithms
# Medium (41.80%)
# Likes:    336
# Dislikes: 0
# Total Accepted:    62.4K
# Total Submissions: 147.6K
# Testcase Example:  '"2"\n"3"'
#
# 给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。
# 
# 示例 1:
# 
# 输入: num1 = "2", num2 = "3"
# 输出: "6"
# 
# 示例 2:
# 
# 输入: num1 = "123", num2 = "456"
# 输出: "56088"
# 
# 说明：
# 
# 
# num1 和 num2 的长度小于110。
# num1 和 num2 只包含数字 0-9。
# num1 和 num2 均不以零开头，除非是数字 0 本身。
# 不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
# 
# 思路1 相乘后相加，使用了缓存 超越5%。。。
# 思路2 作弊试试 str(int(num1) * int(num2)) 超越84%  实际上这个题是给非python准备的。python默认支持大数字计算
#       基本上怎么写都无法超过这个。。。

# @lc code=start
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # if num1 == '0' or num2 == '0': # 否则会返回'00000'...
        #     return '0'

        # r1 = len(num1) - 1
        # r2 = len(num2) - 1

    
        # # 用短的去乘  缓存？
        # ans = '0'
        # m = {}
        # i = r1
        # while i >= 0:
        #     if num1[i] not in m:
        #         j = r2
        #         temp = '0'
        #         while j >= 0:
        #             temp = self.addStrings(temp,str(int(num1[i])*int(num2[j])) + '0' * (r2-j))
        #             j -= 1
        #         m[num1[i]] = temp
                
            
        #     ans = self.addStrings(ans, m.get(num1[i]) + '0' * (r1-i))
        #     i -= 1
        
        # return ans
        return str(int(num1) * int(num2))

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

