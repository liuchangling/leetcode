#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
# 假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−2**31,  2**31 − 1]。
# 请根据这个假设，如果反转后整数溢出那么就返回 0。
# 方案1: 转字符串，切片，转会int 就搞定了。实际上，传入 ‘-123’就错啦.需要特殊处理一下
# 这种方法的问题，判断多，转换类型多，还涉及字符串拼接操作，导致速度只打败66%
# 方案2: 有没有办法通过纯数字搞定这个问题？
#  q = x % 10
#  r = 10 * r + q 咦 结果也是66.72% 哈哈哈哈哈
#  方法3 
#  原因找到了，leetcode需要注意下，把max值放到类属性里面就可以提高很多速度
#  猜测后台跑测试时，如果每次都读取第一行，会消耗时间的。如果在Solution里面，那就只需要读一遍。。。
#  呵呵了


# @lc code=start

class Solution:
    # def reverse(self, x: int) -> int:
    #     s = str(x)
    #     if s.startswith('-'):
    #         rev = int('-' + str(x)[-1:0:-1])
    #     else:
    #         rev = int(str(x)[-1::-1])

    #     if rev < min or rev > max:
    #         return 0
    #     else:
    #         return rev
    def __init__(self):
        self.max10 = (2 ** 31 - 1) // 10

    def reverse(self, x: int) -> int:
        ret = 0
        isNegative = x < 0
        if isNegative:
            x = -x

        while x != 0:
            q = x % 10
            x = x // 10
            if ret > self.max10 or (ret == self.max10 and q > 7):
                return 0
            else:
                ret = ret * 10 + q

        if isNegative:
            ret = -ret

        return ret


# @lc code=end
