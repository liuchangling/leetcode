#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#
# 第一反应使用栈操作诶
# 第一种写法已经很好了,时间和效率都很不错
# 唯一的问题是代码重复率太高，尝试重构一下，
# 方法二，借用dict 减少代码长度
# 看了一波答案
# 方法三，不借用dict的实现，比较技巧了
# 靠着push相反的括号，直接实现

# @lc code=start
class Solution:
    # 方法1 直觉的栈写法
    # def isValid(self, s: str) -> bool:
    #     stack = []
    #     for c in s:
    #         if c == '(' or c == '{' or c == '[':
    #             stack.append(c)
    #         elif c == ')':
    #             if len(stack) == 0:
    #                 return False
    #             elif stack[-1] == '(':
    #                 stack.pop()
    #             else:
    #                 return False
    #         elif c == ']':
    #             if len(stack) == 0:
    #                 return False
    #             elif stack[-1] == '[':
    #                 stack.pop()
    #             else:
    #                 return False
    #         elif c == '}':
    #             if len(stack) == 0:
    #                 return False
    #             elif stack[-1] == '{':
    #                 stack.pop()
    #             else:
    #                 return False

    #     return len(stack) == 0
    
    # 方法2
    # def isValid(self, s: str) -> bool:
    #     stack = []
    #     blocks = {')':'(', ']':'[','}':'{'}
    #     # 感觉也很不舒服，因为实际上运行keys和values也要时间，单独写在循环体外面吧。
    #     # 像这种只涉及3个的，用dict体现不出来性能。如果有个几百上千的话，这种比较好
    #     keys = blocks.keys()
    #     values = blocks.values()
    #     for c in s:
    #         if c in values:
    #             stack.append(c)
    #         elif c in keys:
    #             if len(stack) == 0:
    #                 return False
    #             elif stack[-1] == blocks[c]:
    #                 stack.pop()
    #             else:
    #                 return False

    #     return len(stack) == 0


    # 方法三
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == '(':
                stack.append(')')
            elif c == '[':
                stack.append(']')
            elif c == '{':
                stack.append('}')
            elif c == ')' or c ==']' or c =='}':
                if len(stack) == 0:
                    return False
                else:
                    if c != stack.pop():
                        return False
        
        return len(stack) == 0

# print(Solution().isValid('{()}'))

# @lc code=end

