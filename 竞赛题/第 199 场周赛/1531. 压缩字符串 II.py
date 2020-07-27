# 行程长度编码 是一种常用的字符串压缩方法，它将连续的相同字符（重复 2 次或更多次）替换为字符和表示字符计数的数字（行程长度）。例如，用此方法压缩字符串 "aabccc" ，将 "aa" 替换为 "a2" ，"ccc" 替换为` "c3" 。因此压缩后的字符串变为 "a2bc3" 。

# 注意，本问题中，压缩时没有在单个字符后附加计数 '1' 。

# 给你一个字符串 s 和一个整数 k 。你需要从字符串 s 中删除最多 k 个字符，以使 s 的行程长度编码长度最小。

# 请你返回删除最多 k 个字符后，s 行程长度编码的最小长度 。

 

# 示例 1：

# 输入：s = "aaabcccd", k = 2
# 输出：4
# 解释：在不删除任何内容的情况下，压缩后的字符串是 "a3bc3d" ，长度为 6 。最优的方案是删除 'b' 和 'd'，这样一来，压缩后的字符串为 "a3c3" ，长度是 4 。
# 示例 2：

# 输入：s = "aabbaa", k = 2
# 输出：2
# 解释：如果删去两个 'b' 字符，那么压缩后的字符串是长度为 2 的 "a4" 。
# 示例 3：

# 输入：s = "aaaaaaaaaaa", k = 0
# 输出：3
# 解释：由于 k 等于 0 ，不能删去任何字符。压缩后的字符串是 "a11" ，长度为 3 。
 

# 提示：

# 1 <= s.length <= 100
# 0 <= k <= s.length
# s 仅包含小写英文字母

# 这是个比较难的dp题
# 首先要考虑到逆序思考，把题目转化为选择一个长度为 len(s) - k的子串，使得压缩后长度最小
# dp定义：dp[i][j]表示 从前i个字符即s[:i]删除j个字符的最优长度
# dp初始化：显然对于j>i dp[i][j] = 0 
# dp[0][0] = 0, dp[1][0] = 1
# 状态转移方程：
# 分为用和不用s[i+1]两种情况考虑
# 如果删除字符s[i] 很简单 dp[i][j+1] = dp[i-1][j]
# 如果保留字符s[i] 依然是复用dp[i-1][j]的子问题解。
#   不过这次，我们往后遍历，选用足够多的连续s[i]，最远到达删去不同字符数目为k-j+1 停止
#   再理解一下，这个情况我们考虑的不再单纯是dp[i][j+1] 而是dp[m][j+diff] = dp[i-1][j] + self.count(same)
#   含义为从s[i]开始选用连续same个s[i]

#1764 ms
class Solution:
    def count(self, same:int) -> int:
        # 计算个数到压缩后的字符长度
        if same <= 1 : return 1
        if same < 10 : return 2
        if same < 100 : return 3
        return 4

    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        size = len(s)
        dp = [[100] * (k+1) for _ in range(size + 1)]

        dp[0][0] = 0 
        
        for i in range(1, size + 1): # 从左到右遍历s
            for j in range(0, min(i,k) + 1): # 删除0~j个字符，更新dp，显然j不能大于k和i的最小值
                # 删除s[i-1]的场景
                if j < k : # j == k 不能再删s[i-1]
                    dp[i][j+1] = min(dp[i][j+1], dp[i-1][j])
                
               
                # 使用s[i-1]的场景
                # 注意即使j==k 也可以继续添加字符，直到s遍历到尾部
                # 比较神奇的dp思路，这里根据s[i-1]直接优化后续的dp数组。
                # 这个过程后续会重复多次
                same = 0 # 计算 s[i:]中和s[i-1]相同的字符数
                diff = 0 # 计算 s[i:]中和s[i-1]不同的字符数

                for last in range(i, size+1):  # i~size
                    if s[last-1] == s[i-1]: # 遇到相同字符
                        same += 1 
                    else: # 遇到不同字符 直接尝试删除
                        diff += 1
                    
                    if j + diff <= k: # 最大删除数目为k, 多了没用, 而且越界
                        # 在前i-1个字符中删除了j个字符， 然后选用了same个s[i-1]。其中删除了diff个不同字符
                        dp[last][j+diff] = min(dp[last][j+diff], dp[i-1][j] + self.count(same))
                    else: #删多了，跑
                        break
        
     


        return dp[size][k]




print(Solution().getLengthOfOptimalCompression("aaabcccd", 2))
# print(Solution().getLengthOfOptimalCompression("aabbaa", 2))
# print(Solution().getLengthOfOptimalCompression("aaaaaaaaaaa", 0))