#
# @lc app=leetcode.cn id=231 lang=python3
#
# [231] 2的幂
# 第一反应看二进制是否work int(str(bin(n))[3:]) == 0
# 跑赢92% 
# 2b的一点是， 这个题目认为 0不属于2的n次方。呵呵

## 高级解法 与运算搞定 跑赢92%。代码短一些
# 恒有 n & (n - 1) == 0，这是因为：
# n 二进制最高位为 1，其余所有位为 0；
# n−1 二进制最高位为 0，其余所有位为 1；


# @lc code=start
class Solution:
    # def isPowerOfTwo(self, n: int) -> bool:
    #     bstr = str(bin(n))[2:]
    #     if len(bstr) == 1 :
    #         return bstr == '1'
    #     else :
    #         return int(bstr[1:]) == 0

    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0  and n & (n-1) == 0
     
        
# @lc code=end

