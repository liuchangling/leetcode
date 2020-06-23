#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] 二进制求和
#
# https://leetcode-cn.com/problems/add-binary/description/
#
# algorithms
# Easy (52.16%)
# Likes:    391
# Dislikes: 0
# Total Accepted:    93.4K
# Total Submissions: 175.3K
# Testcase Example:  '"11"\n"1"'
#
# 给你两个二进制字符串，返回它们的和（用二进制表示）。
# 
# 输入为 非空 字符串且只包含数字 1 和 0。
# 
# 
# 
# 示例 1:
# 
# 输入: a = "11", b = "1"
# 输出: "100"
# 
# 示例 2:
# 
# 输入: a = "1010", b = "1011"
# 输出: "10101"
# 
# 
# 
# 提示：
# 
# 
# 每个字符串仅由字符 '0' 或 '1' 组成。
# 1 <= a.length, b.length <= 10^4
# 字符串如果不是 "0" ，就都不含前导零。
# 
# 
# 手写 44ms 67%
# api 36ms 94%
 

# @lc code=start
class Solution:
    # def addBinary(self, a: str, b: str) -> str:        
    #     lena, lenb = len(a), len(b)
    #     ans, i, m, carry = '', 1, max(lena, lenb), False

    #     def add(ta, tb, c):
    #         if c:
    #             if (ta == '1' and tb == '0') or (ta == '0' and tb =='1'):
    #                 return ('0', True)
    #             elif ta == '1' and tb == '1':
    #                 return ('1', True)
    #             else :
    #                 return ('1', False)
    #         else:
    #             if (ta == '1' and tb == '0') or (ta == '0' and tb =='1'):
    #                 return ('1', False)
    #             elif ta == '1' and tb == '1':
    #                 return ('0', True)
    #             else :
    #                 return ('0', False)

    #     while carry or i <= m:
    #         ta = a[lena-i] if i <= lena else '0'
    #         tb = b[lenb-i] if i <= lenb else '0'
    #         t, carry = add(ta, tb, carry)
    #         ans = t + ans
    #         i += 1
        

    #     return ans

    # 36ms 94%
    def addBinary(self, a: str, b: str) -> str:        

        c = int(a,2)+int(b,2)
        return bin(c).replace('0b','')


    #    64ms 8%
    # def addBinary(self, a: str, b: str) -> str:        
    #     lena, lenb = len(a), len(b)
    #     ans, i, m, carry = '', 1, max(lena, lenb), '0'

    #     def add(ta, tb, c):
    #         count = 0
    #         if ta == '1' : count += 1
    #         if tb == '1' : count += 1
    #         if c == '1' : count += 1
    #         newt = '1' if count % 2 == 1 else '0'
    #         newc = '1' if count > 1 else '0'
    #         return (newt, newc)

    #     while carry == '1' or i <= m:
    #         ta = a[lena-i] if i <= lena else '0'
    #         tb = b[lenb-i] if i <= lenb else '0'
    #         t, carry = add(ta, tb, carry)
    #         ans = t + ans
    #         i += 1
        

    #     return ans
        
# @lc code=end

# print(Solution().addBinary("11" , "1"))