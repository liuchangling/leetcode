# 给你一个字符串 s ，请你返回满足以下条件的最长子字符串的长度：每个元音字母，即 'a'，'e'，'i'，'o'，'u' ，在子字符串中都恰好出现了偶数次。

#  

# 示例 1：

# 输入：s = "eleetminicoworoep"
# 输出：13
# 解释：最长子字符串是 "leetminicowor" ，它包含 e，i，o 各 2 个，以及 0 个 a，u 。
# 示例 2：

# 输入：s = "leetcodeisgreat"
# 输出：5
# 解释：最长子字符串是 "leetc" ，其中包含 2 个 e 。
# 示例 3：

# 输入：s = "bcbcbc"
# 输出：6
# 解释：这个示例中，字符串 "bcbcbc" 本身就是最长的，因为所有的元音 a，e，i，o，u 都出现了 0 次。
class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        count = 0 # 统计最长长度
        status = 0 # 默认状态全0
        firstPlace = [-1] * 32 # 用于存储对应状态第一次出现的位置
        firstPlace[0] = 0 # 这是一个默认状态

        m = {'a':1, 'e':2, 'i':4, 'o':8, 'u':16}

        for index in range(len(s)):
            if s[index] in m:
                # 遇到元音，翻转对应状态
                status = status ^ m[s[index]]
            
            # 这里两个分支都有+1  因为有个默认的firstPlace[0] = 0 同时加1避免一些分支判断
            if firstPlace[status] == -1:
                firstPlace[status] = index + 1 # 之前未出现过时，记录当前index 
            else :
                count = max(count, index - firstPlace[status] + 1) # 否则更新count
        

        return count