# 分割字符串的方案数 

# 给你一个二进制串 s  （一个只包含 0 和 1 的字符串），我们可以将 s 分割成 3 个 非空 字符串 s1, s2, s3 （s1 + s2 + s3 = s）。

# 请你返回分割 s 的方案数，满足 s1，s2 和 s3 中字符 '1' 的数目相同。

# 由于答案可能很大，请将它对 10^9 + 7 取余后返回。


# 示例 1：

# 输入：s = "10101"
# 输出：4
# 解释：总共有 4 种方法将 s 分割成含有 '1' 数目相同的三个子字符串。
# "1|010|1"
# "1|01|01"
# "10|10|1"
# "10|1|01"
# 示例 2：

# 输入：s = "1001"
# 输出：0
# 示例 3：

# 输入：s = "0000"
# 输出：3
# 解释：总共有 3 种分割 s 的方法。
# "0|0|00"
# "0|00|0"
# "00|0|0"
# 示例 4：

# 输入：s = "100100010100110"
# 输出：12




# 提示：

# s[i] == '0' 或者 s[i] == '1'
# 3 <= s.length <= 10^5

# 很明显 1个数不能被3整除 返回0
# 
	# 140 ms
# class Solution:
#     def numWays(self, s: str) -> int:
      

#         size = len(s)
#         if size < 3: return 0

#         count = 0
#         for ch in s:
#             if ch == '1':
#                 count += 1

#         if count % 3 != 0 :
#             return 0

#         oneNumbers = count // 3

#         if oneNumbers == 0 :
#             return int( ((size-1)*(size-2)/2) % 1000000007 )


#         zeros = []

#         tempOne = 0
#         tempZero = 0
#         flag = True
#         for ch in s:
#             if ch == '1':
#                 tempOne += 1
#                 flag = False
#                 if tempOne == oneNumbers:
#                     zeros.append(tempZero)
#                     flag = True
#                     tempZero = 0 
#                     tempOne = 0 

#             elif flag == True:
#                 tempZero += 1

#         print(zeros)

#         zeros = zeros[1:]

#         print(zeros)

#         ret = 1
#         for i in zeros :
#             ret = (i+1) * ret

#         print(ret)

#         return int(ret % 1000000007)

# print(Solution().numWays("0000"))


# 赛后发现 3是一个hard code 的值。。。 184ms
class Solution:
    def numWays(self, s: str) -> int:
        size = len(s)
        count = s.count("1")

        if count % 3 != 0 : return 0
        if count == 0 : return int(((size-1)*(size-2)/2) % 1000000007 )
        
        n = count / 3

        c = c1 = c2 = 0
        for ch in s:
            if ch == '1':
                c += 1

            if c == n: # 计算第一个组最后一个1到第二组第一个1之间前的字符数 = 0的个数+1
                c1 += 1
            
            if c == 2 * n:
                c2 += 1
        
        return c1 * c2 % 1000000007 
           

class Solution:
    def numWays(self, s: str) -> int:      
        size = len(s)
        count = s.count("1")

        if count % 3 != 0 : return 0
        if count == 0 : return int(((size-1)*(size-2)/2) % 1000000007 )
        
        n = count / 3

        c = c1 = c2 = 0
        flag = False
        for ch in s:
            if ch == '1':
                c += 1
                flag = c % n == 0
            elif flag:
                # 计算第一个组最后一个1到第二组第一个1之间前的字符数 = 0的个数 最后再+1
                # 这样的好处是避免了全1的字符串重复判断
                if c == n:
                    c1 += 1
                
                if c == 2 * n:
                    c2 += 1
            
        return (c1+1) * (c2+1) % 1000000007 
