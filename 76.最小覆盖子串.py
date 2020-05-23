#
# @lc app=leetcode.cn id=76 lang=python3
#
# [76] 最小覆盖子串
#
# https://leetcode-cn.com/problems/minimum-window-substring/description/
#
# algorithms
# Hard (36.04%)
# Likes:    522
# Dislikes: 0
# Total Accepted:    46.8K
# Total Submissions: 126.3K
# Testcase Example:  '"ADOBECODEBANC"\n"ABC"'
#
# 给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。
# 
# 示例：
# 
# 输入: S = "ADOBECODEBANC", T = "ABC"
# 输出: "BANC"
# 
# 说明：
# 
# 
# 如果 S 中不存这样的子串，则返回空字符串 ""。
# 如果 S 中存在这样的子串，我们保证它是唯一的答案。
# 
# 本题考查的是滑动窗口。  
# 滑动窗口和双指针都是针对于暴力法的优化，可以去除掉很多无需考虑的子区间
# 这个题只考虑是否包含字符，不要求顺序和t中一样。 另外t是可以有重复字符的


# 思路1 40% 代码简单
# 滑动窗口， 右窗口先移动
# 判断是否满足只需要比较出现字符次数即可
# 滑动窗口代码的格式总是：
# for ( r = 0 ; r < length ; r++){
#     # 过滤 & 处理
#     window.handle(array[r])

#     while( canRemove ){
#         window.remove(array[l])
#         l++;
#     }
# }


#  思路2 优化了存储。 mem同时也会将无需计数的字符统计进去，之后通过正负来搞定。省去了很多not in和in的代码
#        另外用了两个int来处理ans ，而非反复对字符串切片

# @lc code=start
class Solution:
    # def minWindow(self, s: str, t: str) -> str:
    #     import collections
    #     need = collections.Counter(t) # 记录t中每个字符有多少次
        
    #     l = meets = 0
    #     ans = ''
        
    #     for r, char in enumerate(s):
    #         if char not in need:
    #             continue
            
    #         need[char] -= 1
    #         if need[char] == 0:
    #             meets += 1 # 该字符已经满足需求

            
    #         while s[l] not in need or need[s[l]] < 0:
    #             # 左侧字符如果可以移除，就让l++ 并更新相应的needs
    #             if  s[l] in need:
    #                 need[s[l]] += 1

    #             l += 1


    #         if meets == len(need):
    #             # 更新ans if necessary
    #             if not ans or len(ans) > r - l + 1:
    #                 ans = s[l: r + 1]

            
    #     return ans


    # 优化后
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        mem = defaultdict(int)
        for char in t:
            mem[char] += 1

        print(mem)
        

        t_len = len(t) # 记录有多少个尚未满足
        left = 0
        
        # 取消了频繁字符串切片的过程 使用int处理
        minLeft = 0
        minRight = len(s)
        
        for right, char in enumerate(s):
            if mem[char] > 0:
                t_len -= 1 # 找到必须的char之后 tlen标记-1

            mem[char] -= 1 # 这里会把之前无需处理的字符也放进去，从0变成负数, 取消了很多in和not in的判断。很妙
            if t_len == 0: 
                #当前窗口已满足条件
                while mem[s[left]] < 0: # 左侧为为非必须时
                    mem[s[left]] += 1 # 更新mem
                    left += 1 # 左边收紧
                if right-left < minRight-minLeft:
                    minLeft, minRight = left, right
                mem[s[left]] += 1
                t_len += 1
                left += 1

        return '' if minRight==len(s) else s[minLeft:minRight+1]
# @lc code=end
