#
# @lc app=leetcode.cn id=739 lang=python3
#
# [739] 每日温度
#
# https://leetcode-cn.com/problems/daily-temperatures/description/
#
# algorithms
# Medium (58.78%)
# Likes:    354
# Dislikes: 0
# Total Accepted:    58.1K
# Total Submissions: 93.7K
# Testcase Example:  '[73,74,75,71,69,72,76,73]'
#
# 根据每日 气温 列表，请重新生成一个列表，对应位置的输出是需要再等待多久温度才会升高超过该日的天数。如果之后都不会升高，请在该位置用 0 来代替。
# 
# 例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4,
# 2, 1, 1, 0, 0]。
# 
# 提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。
# 
# 思路1 散列表+逆序
# 时间1100ms 击败5%。时间复杂度最坏情况是O(mn)
# 
# 思路2 数组+逆序
# 时间1700 击败5% 时间复杂度和1相同

# 思路3 单调栈
# 栈底到栈顶温度单调不增，保存下标
# 遇到未增加的温度就入栈
# 遇到更大的温度，不停出栈直到能入栈再入栈

# @lc code=start
class Solution:
    # 思路1  1100ms
    # def dailyTemperatures(self, T: List[int]) -> List[int]:
    #     dic = defaultdict(int)
    #     size = len(T)
    #     ans = [0 for i in range(size)]

    #     for i in range(size - 1, -1, -1):
    #         n = T[i]
    #         minIndex = size
    #         dic[n] = i
    #         for key in dic:
    #             if key > n  :
    #                 minIndex = min(minIndex, dic[key])
            
    #         if minIndex < size:
    #             ans[i] = minIndex - i
        
    #     return ans

    # 思路2  1700ms
    # def dailyTemperatures(self, T: List[int]) -> List[int]:
    #     size = len(T)
    #     ans = [0 for i in range(size)]
    #     temp = [0 for j in range(71)]

    #     for i in range(size - 1, -1, -1):
    #         for j in range(71):
    #             if j + 30 < T[i]:
    #                 temp[j] = i

    #         ans[i] = max(temp[T[i] - 30] - i , 0)

    #     return ans

    # 思路3  544ms
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack, size = [], len(T)
        
        ans = [0 for i in range(size)]

        for i in range(size):
            while stack and T[stack[-1]] < T[i]:
                tmpIndex = stack.pop()
                ans[tmpIndex] = i - tmpIndex
            stack.append(i) 

        return ans
        
# @lc code=end

