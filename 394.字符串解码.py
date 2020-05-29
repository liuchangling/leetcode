#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] 字符串解码
#
# https://leetcode-cn.com/problems/decode-string/description/
#
# algorithms
# Medium (48.74%)
# Likes:    322
# Dislikes: 0
# Total Accepted:    36.6K
# Total Submissions: 70.8K
# Testcase Example:  '"3[a]2[bc]"'
#
# 给定一个经过编码的字符串，返回它解码后的字符串。
#
# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。
#
# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
#
# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。
#
# 示例:
#
#
# s = "3[a]2[bc]", 返回 "aaabcbc".
# s = "3[a2[c]]", 返回 "accaccacc".
# s = "2[abc]3[cd]ef", 返回 "abcabccdcdcdef".
#
#
#

# @lc code=start

# 乍一看，要么递归要么栈
# 编译一般都用栈，那就写一个栈的

# 思路1 栈： 94%
# 遇到]直接取出[]之间的字符串。如果[左侧是数字，则相乘
# 遇到数字入栈，如果是连续数字进行拼接
# 遇到[, 字符，直接入栈
# 最终栈里面是多个字符串，直接相加即可

# 使用了isdigit 的api 只插入字符， 更慢了, 略

# 思路2 辅助栈：82%
# 代码简洁一些 实测比1慢一点，代码较难想到.也可以字母和数字分开两栈实现
#       代码会好懂一点
# 构建辅助栈 stack， 遍历字符串 s 中每个字符 c；
# 当 c 为数字时，将数字字符转化为数字 multi，用于后续倍数计算；
# 当 c 为字母时，在 res 尾部添加 c；
# 当 c 为 [ 时，将当前 multi 和 res 入栈，并分别置空置 0：
#   记录此 [ 前的临时结果 res 至栈，用于发现对应 ] 后的拼接操作；
#   记录此 [ 前的倍数 multi 至栈，用于发现对应 ] 后，获取 multi × [...] 字符串。
#   进入到新 [ 后，res 和 multi 重新记录。
# 当 c 为 ] 时，stack 出栈，拼接字符串 res = last_res + cur_multi * res，其中:
#   last_res是上个 [ 到当前 [ 的字符串，例如 "3[a2[c]]" 中的 a；
#   cur_multi是当前 [ 到 ] 内字符串的重复倍数，例如 "3[a2[c]]" 中的 2。
# 返回字符串 res。

# 思路3 正则 94%
#      循环多次正则匹配，如果找到数字[字符] 就replace。直到无法匹配上

# 思路4 递归
# 栈的写法通常都可以递归

class Solution:
    # 栈 94%
    def decodeString(self, s):
        stack = []

        for ch in s:
            if ch == ']':
                p = stack.pop()
                t = ''
                while p != '[':
                    if type(p) == int:
                        t *= p
                    else:
                        t = p + t
                    p = stack.pop()

                if len(stack) > 0 and type(stack[-1]) == int:
                    t *= stack.pop()

                stack.append(t)

            elif '0' <= ch <= '9':
                n = int(ch)
                if len(stack) > 0 and type(stack[-1]) == int:
                    stack[-1] = stack[-1] * 10 + n
                else:
                    stack.append(n)
            else:
                stack.append(ch)
        return ''.join(stack)

    # 辅助栈 82%
    # def decodeString(self, s: str) -> str:
    #     stack, res, multi = [], "", 0
    #     for c in s:
    #         if c == '[':
    #             stack.append([multi, res])
    #             res, multi = "", 0
    #         elif c == ']':
    #             cur_multi, last_res = stack.pop()
    #             res = last_res + cur_multi * res
    #         elif '0' <= c <= '9':
    #             multi = multi * 10 + int(c)
    #         else:
    #             res += c
    #     return res

    # 正则 大神版。。
    # def decodeString(self,s:str)->str:
    #     pattern=re.compile(r'(\d+)\[(\w+)\]')
    #     m=pattern.findall(s)
    #     while m:
    #         for num,char in m:
    #             s=s.replace(f'{num}[{char}]',char*int(num))
    #         m=pattern.findall(s)
    #     return s

    # 递归 62%
    # def decodeString(self,s:str)->str:
    #     def dfs(s, i):
    #         res, multi = "", 0
    #         while i < len(s):
    #             if '0' <= s[i] <= '9':
    #                 multi = multi * 10 + int(s[i])
    #             elif s[i] == '[':
    #                 tmp, i = dfs(s, i + 1) # [开启递归
    #                 res += multi * tmp
    #                 multi = 0
    #             elif s[i] == ']':
    #                 return res, i # ]结束递归
    #             else:
    #                 res += s[i]
    #             i += 1
    #         return res, i
    #     return dfs(s,0)[0]


# Solution().decodeString("3[a2[c]]")

# @lc code=end
