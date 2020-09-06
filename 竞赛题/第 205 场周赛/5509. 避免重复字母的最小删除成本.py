# 给你一个字符串 s 和一个整数数组 cost ，其中 cost[i] 是从 s 中删除字符 i 的代价。

# 返回使字符串任意相邻两个字母不相同的最小删除成本。

# 请注意，删除一个字符后，删除其他字符的成本不会改变。

 

# 示例 1：

# 输入：s = "abaac", cost = [1,2,3,4,5]
# 输出：3
# 解释：删除字母 "a" 的成本为 3，然后得到 "abac"（字符串中相邻两个字母不相同）。
# 示例 2：

# 输入：s = "abc", cost = [1,2,3]
# 输出：0
# 解释：无需删除任何字母，因为字符串中不存在相邻两个字母相同的情况。
# 示例 3：

# 输入：s = "aabaa", cost = [1,2,3,4,1]
# 输出：2
# 解释：删除第一个和最后一个字母，得到字符串 ("aba") 。
 

# 提示：

# s.length == cost.length
# 1 <= s.length, cost.length <= 10^5
# 1 <= cost[i] <= 10^4
# s 中只含有小写英文字母

# 如果遇到连续重复，就二选一删掉一个
from typing import List

class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        
        size = len(s)
        ret = 0 
        
        lastCh = ''
        startIdx = -1
        endIdx = -2

        for i in range(size):
            if s[i] != lastCh:
                # 终止重复
                if endIdx == i - 1:
                    tmp = cost[startIdx: endIdx+1]
                    ret += sum(tmp) - max(tmp)
                lastCh = s[i]
                startIdx = i
            elif s[i] == lastCh:
                # 遇到重复
                endIdx = i
                if i == size - 1:
                    tmp = cost[startIdx: endIdx+1]
                    ret += sum(tmp) - max(tmp)
        return ret

print(Solution().minCost("aabaa", [1,2,3,4,1]))