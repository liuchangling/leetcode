#
# @lc app=leetcode.cn id=557 lang=python3
#
# [557] 反转字符串中的单词 III
# 思路1 先split 然后reverse ，遍历reverse ，最后join 80%
#      return ' '.join([i[::-1] for i in s.split(' ')])
# 思路2 玩玩栈 效率28%。。。
# 思路3 反转后直接拼接，再reverse。spilt reverse join reverse 97%

# @lc code=start
class Solution:
    # def reverseWords(self, s: str) -> str:
    #     return ' '.join([i[::-1] for i in s.split(' ')])

    # def reverseWords(self, s: str) -> str:
    #     stack = []
    #     ret = ''
    #     for char in s:
    #         if char == ' ':
    #             stack.reverse()
    #             ret += ''.join(stack) + ' '
    #             stack = []
    #         else:
    #             stack.append(char)
        
    #     stack.reverse()
    #     ret += ''.join(stack)
        
    #     return ret

    def reverseWords(self, s: str) -> str:
        return ' '.join(s.split(' ')[::-1])[::-1]
        
# @lc code=end

