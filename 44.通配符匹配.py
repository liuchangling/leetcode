#
# @lc app=leetcode.cn id=44 lang=python3
#
# [44] 通配符匹配
#
# https://leetcode-cn.com/problems/wildcard-matching/description/
#
# algorithms
# Hard (27.62%)
# Likes:    384
# Dislikes: 0
# Total Accepted:    33.2K
# Total Submissions: 118.1K
# Testcase Example:  '"aa"\n"a"'
#
# 给定一个字符串 (s) 和一个字符模式 (p) ，实现一个支持 '?' 和 '*' 的通配符匹配。
# 
# '?' 可以匹配任何单个字符。
# '*' 可以匹配任意字符串（包括空字符串）。
# 
# 
# 两个字符串完全匹配才算匹配成功。
# 
# 说明:
# 
# 
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 ? 和 *。
# 
# 
# 示例 1:
# 
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
# 
# 示例 2:
# 
# 输入:
# s = "aa"
# p = "*"
# 输出: true
# 解释: '*' 可以匹配任意字符串。
# 
# 
# 示例 3:
# 
# 输入:
# s = "cb"
# p = "?a"
# 输出: false
# 解释: '?' 可以匹配 'c', 但第二个 'a' 无法匹配 'b'。
# 
# 
# 示例 4:
# 
# 输入:
# s = "adceb"
# p = "*a*b"
# 输出: true
# 解释: 第一个 '*' 可以匹配空字符串, 第二个 '*' 可以匹配字符串 "dce".
# 
# 
# 示例 5:
# 
# 输入:
# s = "acdcb"
# p = "a*c?b"
# 输出: false
# 

# 思路1  dp 972ms 38%
# 动态规划
# 定义 dp[i][j] 表示字符串 s 的前 i 个字符和模式 p 的前 j 个字符是否能匹配。
#
# 动态转移方程
# 如果 p[j]是小写字母，那么 s[i]必须也为相同的小写字母，dp[i][j]= s[i]==p[j] and dp[i−1][j−1]
# 如果 p[j]  == '?' 那么对 s[i] 没有任何要求，状态转移方程为：dp[i][j] = dp[i-1][j-1]
# 如果 p[j]  == '*'那么同样对s[i]没有任何要求，
# 但是星号可以匹配零或任意多个小写字母，因此状态转移方程分为两种情况，即使用或不使用这个星号
# dp[i][j]=dp[i][j−1] or dp[i−1][j]
# 
# 初始状态
# p[0][0] = True，即当字符串 s 和模式 p 均为空时，匹配成功；

# dp[i][0] =False，即空模式无法匹配非空字符串；

# dp[0][j] 需要分情况讨论：因为星号才能匹配空字符串，所以只有当模式 p 的前 j 个字符均为星号时，dp[0][j]dp[0][j] 才为真。




# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)

        dp = [[False] * (n + 1) for _ in range(m + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            if p[i - 1] == '*':
                dp[0][i] = True
            else:
                break
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] | dp[i - 1][j]
                elif p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                
        return dp[m][n]

# @lc code=end

