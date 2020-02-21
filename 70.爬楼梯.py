#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#
# https://leetcode-cn.com/problems/climbing-stairs/description/
#
# algorithms
# Easy (47.09%)
# Likes:    843
# Dislikes: 0
# Total Accepted:    135.9K
# Total Submissions: 283.8K
# Testcase Example:  '2'
#
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
# 
# 注意：给定 n 是一个正整数。
# 
# 示例 1：
# 
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
# 
# 示例 2：
# 
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶
# 
# 思路1 动态规划
# 已知 f(1) = 1 f(2) = 2
# 对于f(n) 拆分为2种情况 先走1步 之后f(n-1)种走法；
#                     先走2步，之后f(n-2)种走法
# 所以f(n) = f(n-1) + f(n-2) 
# 递归写法运行超时了，一脸懵逼
# 额 改成了数组下标计算，仅击败8%。。。最近速度怎么这么慢啊

# 思路2 斐波那契数 和思路1差不多，不过将借用的空间缩小，仅用2个变量保存 速度依然8%

# 思路3 Binets 方法 这是一个时间复杂度为lgn的计算方法
#      原理是f(n) = [[1,1], [1,0]]^n

# @lc code=start
class Solution:
    # 思路1 递归版，超时了。。。
    # def climbStairs(self, n: int) -> int:
    #     if n <= 2 :
    #         return n
    #     else :
    #         return self.climbStairs(n-1) + self.climbStairs(n-2)

    # 思路1 非递归版 8%
    # def climbStairs(self, n: int) -> int:
    #     if n < 3 :
    #         return n
    #     a = n * [0]
    #     a[0] = 1
    #     a[1] = 2
    #     for i in range (2, n):
    #         a[i] = a[i-1] + a[i-2]
        
    #     return a[n-1]

    # 思路2 8%
    # def climbStairs(self, n: int) -> int:
    #     if n == 1:
    #         return 1
    #     first = 1
    #     second = 2
    #     for i in range(2,n):
    #         thrid = first + second
    #         first = second
    #         second = thrid
        
    #     return second

    def climbStairs(self, n: int) -> int:
        q = [[1,1], [1,0]]
        p = self.pow(q, n)
        return p[0][0]

    def pow(self, a, n):
        q = [[1,1], [1,0]]
        while n > 0:
            if ( n & 1 )== 1:
                ret = self.multipy(a, q)
            else :
                a = self.multipy(a, a)
                n = n >> 1
        
        return ret

    def multipy(self, a, b):
        c = [[0,0], [0,0]]
        
        for i in range(0,2):
            for j in range(0,2):
                c[i][j] = a[i][0] * b[0][j] + a[i][1] * b[1][j]

        return c 

print(Solution().climbStairs(2))



# @lc code=end

