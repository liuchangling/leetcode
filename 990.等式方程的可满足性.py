#
# @lc app=leetcode.cn id=990 lang=python3
#
# [990] 等式方程的可满足性
#
# https://leetcode-cn.com/problems/satisfiability-of-equality-equations/description/
#
# algorithms
# Medium (40.27%)
# Likes:    50
# Dislikes: 0
# Total Accepted:    6.3K
# Total Submissions: 14.3K
# Testcase Example:  '["a==b","b!=a"]'
#
# 给定一个由表示变量之间关系的字符串方程组成的数组，每个字符串方程 equations[i] 的长度为 4，并采用两种不同的形式之一："a==b" 或
# "a!=b"。在这里，a 和 b 是小写字母（不一定不同），表示单字母变量名。
# 
# 只有当可以将整数分配给变量名，以便满足所有给定的方程时才返回 true，否则返回 false。 
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：["a==b","b!=a"]
# 输出：false
# 解释：如果我们指定，a = 1 且 b = 1，那么可以满足第一个方程，但无法满足第二个方程。没有办法分配变量同时满足这两个方程。
# 
# 
# 示例 2：
# 
# 输出：["b==a","a==b"]
# 输入：true
# 解释：我们可以指定 a = 1 且 b = 1 以满足满足这两个方程。
# 
# 
# 示例 3：
# 
# 输入：["a==b","b==c","a==c"]
# 输出：true
# 
# 
# 示例 4：
# 
# 输入：["a==b","b!=c","c==a"]
# 输出：false
# 
# 
# 示例 5：
# 
# 输入：["c==c","b==d","x!=z"]
# 输出：true
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= equations.length <= 500
# equations[i].length == 4
# equations[i][0] 和 equations[i][3] 是小写字母
# equations[i][1] 要么是 '='，要么是 '!'
# equations[i][2] 是 '='
# 
# 思路1 77%
# 这个题我开始想着设置i=0, 把相等赋值为同一个值， 遇到新的i+=1之后再赋值。
# 这个思路无法解决 a==b , c==d的情况，会很复杂。

# 所以只能从图形连通性的角度考虑。写了一个BFS的，代码实现难度还不低，结果TLE了。。。

# 看了官方题解，这种题目叫并查集DSU(Disjoint Set Union) 这是一种特殊的数据结构。类似森林。
# 里面是多个不相交的集合。
# 开始时让每个元素构成一个单元素的集合，然后按一定顺序将属于同一组的元素所在的集合合并，其间要反复查找一个元素在哪个集合中。

# 个人理解并查集重点就是对于集合的 【并union】 和 【查find】
# 实际实现中也必须包含union和find两步骤。 官方题解代码实现比较严格的遵循了算法导论这一part
# 个人实现中简化了代码，看起来会简单点

# 这题的union的设计为。默认根为自身index， 如果有新的连接关系，就将a的根指向b的根。
# 这样每个equations中就被转化为一系列的转化关系，这里的chs数组更像一个树结构，index表示本身，value指向根，
# index == value表示自己就是根， 挺巧妙的
# find比较简单，就是getroot而已，一路getparent上去即可

# from typing import List
# import collections

# @lc code=start
class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        chs = list(range(26))

        def getRoot(node):
            while chs[node] != node:
                node = chs[node]

            return node


        for equ in equations:
            a = ord(equ[0]) - ord('a')
            b = ord(equ[3]) - ord('a')
            if equ[1] == '=': # union 
                chs[getRoot(a)] = getRoot(b)
        
        for equ in equations:
            a = ord(equ[0]) - ord('a')
            b = ord(equ[3]) - ord('a')
            if equ[1] == '!': # query
                if getRoot(a) == getRoot(b): return False  
    

        return True
        
# @lc code=end

# print(Solution().equationsPossible( ["b==d","c==a","h==a","d==d","a==b","h!=k","i==h"] ))