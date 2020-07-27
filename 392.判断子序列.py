#
# @lc app=leetcode.cn id=392 lang=python3
#
# [392] 判断子序列
#
# https://leetcode-cn.com/problems/is-subsequence/description/
#
# algorithms
# Easy (48.93%)
# Likes:    283
# Dislikes: 0
# Total Accepted:    72.7K
# Total Submissions: 144.7K
# Testcase Example:  '"abc"\n"ahbgdc"'
#
# 给定字符串 s 和 t ，判断 s 是否为 t 的子序列。
# 
# 你可以认为 s 和 t 中仅包含英文小写字母。字符串 t 可能会很长（长度 ~= 500,000），而 s 是个短字符串（长度 <=100）。
# 
# 
# 字符串的一个子序列是原始字符串删除一些（也可以不删除）字符而不改变剩余字符相对位置形成的新字符串。（例如，"ace"是"abcde"的一个子序列，而"aec"不是）。
# 
# 示例 1:
# s = "abc", t = "ahbgdc"
# 
# 返回 true.
# 
# 示例 2:
# s = "axc", t = "ahbgdc"
# 
# 返回 false.
# 
# 后续挑战 :
# 
# 如果有大量输入的 S，称作S1, S2, ... , Sk 其中 k >= 10亿，你需要依次检查它们是否为 T
# 的子序列。在这种情况下，你会怎样改变代码？
# 
# 致谢:
# 
# 特别感谢 @pbrother 添加此问题并且创建所有测试用例。
# 
# 双指针 44ms 时间复杂度 O(len(s) + len(t))
# 

#  
# 思路dp  用于处理后续挑战的
# 对于t进行预处理
# f[i][j] 表示字符串 t 中从位置 i 开始往后字符 j 第一次出现的位置。
# 在进行状态转移时，如果 t 中位置 i 的字符就是 j，那么 f[i][j]==i，
# 否则 j 出现在位置 i+1 开始往后，即 f[i][j]=f[i+1][j]



# @lc code=start

class Solution:
    # 双指针1 44ms
    # def isSubsequence(self, s: str, t: str) -> bool:
    #     p = 0 
    #     for ch in s:
    #         idx = t[p:].find(ch)
    #         # print(idx, t[p:], ch)
    #         if idx < 0 :
    #             return False
    #         else:
    #             p += idx + 1

    #     return True

    # 双指针2 44ms
    # def isSubsequence(self, s: str, t: str) -> bool:
    #     n, m = len(s), len(t)
    #     i = j = 0
    #     while i < n and j < m:
    #         if s[i] == t[j]:
    #             i += 1
    #         j += 1
    #     return i == n


    # dp 168ms
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        f = [[0] * 26 for _ in range(m)]
        f.append([m] * 26)

        for i in range(m - 1, -1, -1):
            for j in range(26):
                f[i][j] = i if ord(t[i]) == j + ord('a') else f[i + 1][j]
        
        add = 0
        for i in range(n):
            if f[add][ord(s[i]) - ord('a')] == m:
                return False
            add = f[add][ord(s[i]) - ord('a')] + 1
        
        return True





# @lc code=end

# print(Solution().isSubsequence("abc", "ahbgdc"))
# print(Solution().isSubsequence("axc", "ahbgdc"))
# print(Solution().isSubsequence("aaaa", "bbaaaa"))