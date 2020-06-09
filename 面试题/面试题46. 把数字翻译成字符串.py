# 面试题46. 把数字翻译成字符串
# 给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。

 

# 示例 1:

# 输入: 12258
# 输出: 5
# 解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi"
 

# 提示：

# 0 <= num < 231


# 思路1  BFS，DFS都可以，每次放入下1位和下2位节点，如果2位大于25就丢弃。
# 如果下一位节点为空。则视为已经找到了一种合法解释。 这个时间复杂度为O(N) 懒得实现了
# 看了一下题解，有DFS+MEMO解决这个问题的，一般dfs出栈就丢弃，这种情况出栈会入栈存起来。记忆化cach

# 思路2 DP 发现如果[11]和[2]后续的可能性是数量相同的，没有必要重新计算。想办法复用结果
# 初始状态 dp[0] = 1 , dp[1]= 2 if str(num)[:2]<'25' else 1
# dp[i]定义为以第i位结尾的可能性总数。
# 如果可以一次2位 那就可以从dp[i-2]过来，否则只能从dp[i-1]过来
# 状态转移方程  dp[i] = dp[i-1] if str(num)[i-1:i+1]>'25' else dp[i-1] + dp[i-2]
# 虽然时间复杂度也是O(n)但是这个去掉了很多无用的计算

# isValid和上述情况没考虑全， 发现506 计算错误了， 因为把06和6考虑成了两种情况， 实际上是一种情况

# 思路3 极简递归DP  94%
# 直接递归用数字处理，不涉及str转化，大佬代码

class Solution:
    #思路 2 Dp 80% 可以优化空间，只保存前两个值而非整个dp数组，这里就不写了
    # def translateNum(self, num: int) -> int:
    #     l = list(str(num))
    #     size = len(l)
    #     if size == 1 : return 1

    #     dp = [0 for i in range(size)]

    #     dp[0] = 1

    #     def isValid(i, j):
    #         if l[i] == '0' : return False # '06' 和 '6' 是同一个解释
    #         return l[i]+l[j] < '26'

    #     dp[1] = 2 if isValid(0,1) else 1

    #     for i in range(2, len(l)):
    #         dp[i] = dp[i-1] + dp[i-2] if isValid(i-1, i) else dp[i-1]
            
    #     print(dp)

    #     return dp[-1]


    # 思路3  大佬代码 无str
    def translateNum(self, num: int) -> int:
        if num < 10 : return 1
        
        if 10 <= num % 100 <= 25 :
            return self.translateNum(num // 10) + self.translateNum(num // 100)
        else :
            return self.translateNum(num // 10)