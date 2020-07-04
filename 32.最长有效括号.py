#
# @lc app=leetcode.cn id=32 lang=python3
#
# [32] 最长有效括号
#
# https://leetcode-cn.com/problems/longest-valid-parentheses/description/
#
# algorithms
# Hard (30.53%)
# Likes:    820
# Dislikes: 0
# Total Accepted:    79.1K
# Total Submissions: 243.9K
# Testcase Example:  '"(()"'
#
# 给定一个只包含 '(' 和 ')' 的字符串，找出最长的包含有效括号的子串的长度。
# 
# 示例 1:
# 
# 输入: "(()"
# 输出: 2
# 解释: 最长有效括号子串为 "()"
# 
# 
# 示例 2:
# 
# 输入: ")()())"
# 输出: 4
# 解释: 最长有效括号子串为 "()()"
# 
# 
# 思路1 栈 60ms
# 对于遇到的每个 ‘(’ ，我们将它的下标放入栈中
# 对于遇到的每个 ‘)’ ，我们先弹出栈顶元素表示匹配了当前右括号：
# 如果栈为空，说明当前的右括号为没有被匹配的右括号，我们将其下标放入栈中来更新我们之前提到的「最后一个没有被匹配的右括号的下标」
# 如果栈不为空，当前右括号的下标减去栈顶元素即为「以该右括号为结尾的最长有效括号的长度」


# 思路2 dp 52ms
# dp[i] 定义为 以s[i]结尾的最长有效括号长度，所以对于(结尾的均为0
# 如何计算dp[i+1]呢？ 如果 s[i-dp[i]-1] == ')'则为0 ，否则就匹配成功要计算了
# 这里动态转移方程分为三个部分
# dp[i+1] = 基础长度(=2) + 内部括号(从 i-dp[i]-1 ~ i) + 外部括号(dp[i-dp[i]-2])

# 思路3 正逆向遍历法 48ms
# 我的天，我一开始直觉思路就是这个最优解，可是想错了什么时候将left和right置0.。。。
# 被一个()(()的测试用例搞蒙了 一直是4不是2.。后来看了题解，加了一个置0操作，然后添加反向遍历就完事了
# 然而我开始反向也想好了。但是没有进行代码实现，也是因为没想好置0的条件。

# @lc code=start
class Solution:
    # 思路1 栈  55% 60ms
    # def longestValidParentheses(self, s: str) -> int:
    #     stack = [-1]  # 栈顶存放最早一次出现未匹配右括号的位置，默认-1
    #     ans = 0 

    #     for idx, ch in enumerate(s):
    #         if ch == '(':
    #             stack.append(idx) # 遇到( 就入栈
    #         else:
    #             i = stack.pop()  # 匹配到的( 先出栈

    #             if not stack:
    #                 stack.append(idx)  # 栈空了，当前idx表示未匹配的右括号下标
    #             else:
    #                 ans = max(ans, idx - stack[-1]) # 上一个未使用的左括号或者右括号的起点，之后都match了
    #     return ans

    # 思路2 dp 52ms 87%     
    # def longestValidParentheses(self, s: str) -> int:
    #     size = len(s)
    #     dp = [0 for _ in range(size)]
    #     ans = 0 

    #     for i in range(1, size):
    #         ch = s[i]
    #         if ch == ')':
    #             matchIdx = i - dp[i-1] - 1
    #             if matchIdx >= 0 and s[matchIdx] == '(': # 匹配成功才计算
    #                 if matchIdx > 0 :
    #                     dp[i] = 2 + dp[i-1] + dp[matchIdx-1]  # ()(())的情况 要把dp[1]加上
    #                 else:
    #                     dp[i] = 2 + dp[i-1] 

    #                 ans = max(ans, dp[i])
            
        
    #     # print(dp)
    #     return ans

    # 正逆向法，空间复杂度o(1) 48ms 95%
    def longestValidParentheses(self, s: str) -> int:
        left, right, ans = 0, 0, 0
        for ch in s :
            if ch == '(':
                left += 1 
            else :
                right += 1
                if left == right :
                    ans = max(ans, left)
                elif right > left: # 注意这个条件，正向遍历时，右括号数目大于左括号数目，就把left和right都搞成0
                    left, right = 0, 0 
        
        left, right = 0, 0 
        for ch in s[::-1]:
            if ch == ')':
                right += 1
            else :
                left += 1
                if left == right :
                    ans = max(ans, left)
                elif right < left:
                    left, right = 0, 0 

        return ans * 2





    
# @lc code=end
# Solution().longestValidParentheses("(()))())(")
# Solution().longestValidParentheses(")()())")
# Solution().longestValidParentheses("()(())")
