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


#  

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        import collections
        need = collections.Counter(t) # 记录t中每个字符有多少次
        
        l = meets = 0
        ans = ''
        
        for r, char in enumerate(s):
            if char not in need:
                continue
            
            need[char] -= 1
            if need[char] == 0:
                meets += 1 # 该字符已经满足需求

            
            while s[l] not in need or need[s[l]] < 0:
                # 左侧字符如果可以移除，就让l++ 并更新相应的needs
                if  s[l] in need:
                    need[s[l]] += 1

                l += 1


            if meets == len(need):
                # 更新ans if necessary
                if not ans or len(ans) > r - l + 1:
                    ans = s[l: r + 1]

            
        return ans

# @lc code=end
