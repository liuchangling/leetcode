#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
# 进阶:你能不将整数转为字符串来解决这个问题吗？


# 方案1 参考第7题，反转比是否相等 速度42.48%
# 方案2 反转数字后一半，看是否和前一半相等
# 方案3 同2 不用math库 速度也很神奇 50 -96不等。感觉leetcode服务器也不稳定
#       方案3有一个提前结束继续判断的定义。 返回判断 //10处理了奇数长度的数字问题，是一个技巧

#import math

# @lc code=start


class Solution:  

    # 方案1 参考第7题，反转比是否相等 速度42.48%
    # def isPalindrome(self, x: int) -> bool:
    # if x < 0:
    #         return False
    #     if  x == 0: # log10(0) exception
    #         return True 
    #     q = 0
    #     s = x
    #     while s != 0:
    #         q = q * 10 + s % 10
    #         s = s // 10

    #     return q == x
    
    #  方案2 依赖math库 速度仅 击败5%
        # length = math.floor(math.log10(x)) + 1
        # right = math.floor(length / 2)
        # i = 0
        # q = 0

        # while i < right:
        #     q = q * 10 + x % 10
        #     x = x // 10

        #     print(i, x, q)
        #     i = i + 1

        # if length % 2 == 1:
        #     x = x // 10

        # return q == x


    # 方案3 注意while结束条件
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False

        if x == 0 :
            return True
        
        if x % 10 == 0:
            return False

        q = 0
        while x > q :
            q = q*10 + x % 10
            x = x//10

        return x == q or x == q // 10
    

# @lc code=end
