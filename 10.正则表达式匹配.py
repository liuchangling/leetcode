#
# @lc app=leetcode.cn id=10 lang=python3
#
# [10] 正则表达式匹配
#
# https://leetcode-cn.com/problems/regular-expression-matching/description/
#
# algorithms
# Hard (27.87%)
# Likes:    1302
# Dislikes: 0
# Total Accepted:    89.8K
# Total Submissions: 307.5K
# Testcase Example:  '"aa"\n"a"'
#
# 给你一个字符串 s 和一个字符规律 p，请你来实现一个支持 '.' 和 '*' 的正则表达式匹配。
# 
# '.' 匹配任意单个字符
# '*' 匹配零个或多个前面的那一个元素
# 
# 
# 所谓匹配，是要涵盖 整个 字符串 s的，而不是部分字符串。
# 
# 说明:
# 
# 
# s 可能为空，且只包含从 a-z 的小写字母。
# p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
# 
# 
# 示例 1:
# 
# 输入:
# s = "aa"
# p = "a"
# 输出: false
# 解释: "a" 无法匹配 "aa" 整个字符串。
# 
# 
# 示例 2:
# 
# 输入:
# s = "aa"
# p = "a*"
# 输出: true
# 解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
# 
# 
# 示例 3:
# 
# 输入:
# s = "ab"
# p = ".*"
# 输出: true
# 解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
# 
# 
# 示例 4:
# 
# 输入:
# s = "aab"
# p = "c*a*b"
# 输出: true
# 解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。
# 
# 
# 示例 5:
# 
# 输入:
# s = "mississippi"
# p = "mis*is*p*."
# 输出: false
# 

# 思路 动态规划
# dp[i][j] 表示s[0~i-1] 和p[0~j-1]是否匹配  
# dp[0][0] 表示两个空字符串匹配，= True
# p[j-1]遇到一个非*的字符  dp[i][j] = d[i-1][j-1] if s[i-1] match p[j-1] else False
# p[j-1]遇到* 有两种情况,看下能否选用p[j-2~j-1]两个通配符
#       情况1 如果s[i-1] match p[j-2] 那么 dp[i][j] = dp[i-1][j] or dp[i][j-2]
#       情况2 如果s[i-1] match p[j-2] 那么 dp[i][j] = dp[i][j-2] 即不可以用p[j-1~j-2]

# 细节注意 
# j需要从1遍历到n+1 而非从0开始
# 需要match需要放置数组越界的问题， 尤其是python负数也有效


# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        
        dp = [[False for i in range(n + 1)] for _ in range(m + 1)]

        dp[0][0] = True

        def match(i: int, j: int) -> bool:
            if i == 0 : return False
            if p[j-1] == '.': return True

            return s[i-1] == p[j-1]

        for i in range(m + 1):
            for j in range(1, n + 1): # 注意j需要从1开始， 否则a* 的第一次p[-1]为* 有问题。
                if p[j-1] == '*':
                    if match(i, j-1) :
                        dp[i][j] = dp[i-1][j] or dp[i][j-2]
                    else :
                        dp[i][j] = dp[i][j-2]
                else :
                    dp[i][j] = dp[i-1][j-1] if match(i, j) else False
        

        return dp[-1][-1]

# @lc code=end



# print(Solution().isMatch("" , "a"))