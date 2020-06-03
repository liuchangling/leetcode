#
# @lc app=leetcode.cn id=838 lang=python3
#
# [838] 推多米诺
#
# https://leetcode-cn.com/problems/push-dominoes/description/
#
# algorithms
# Medium (44.57%)
# Likes:    53
# Dislikes: 0
# Total Accepted:    3.3K
# Total Submissions: 7.3K
# Testcase Example:  '".L.R...LR..L.."'
#
# 一行中有 N 张多米诺骨牌，我们将每张多米诺骨牌垂直竖立。
#
# 在开始时，我们同时把一些多米诺骨牌向左或向右推。
#
#
#
# 每过一秒，倒向左边的多米诺骨牌会推动其左侧相邻的多米诺骨牌。
#
# 同样地，倒向右边的多米诺骨牌也会推动竖立在其右侧的相邻多米诺骨牌。
#
# 如果同时有多米诺骨牌落在一张垂直竖立的多米诺骨牌的两边，由于受力平衡， 该骨牌仍然保持不变。
#
# 就这个问题而言，我们会认为正在下降的多米诺骨牌不会对其它正在下降或已经下降的多米诺骨牌施加额外的力。
#
# 给定表示初始状态的字符串 "S" 。如果第 i 张多米诺骨牌被推向左边，则 S[i] = 'L'；如果第 i 张多米诺骨牌被推向右边，则 S[i] =
# 'R'；如果第 i 张多米诺骨牌没有被推动，则 S[i] = '.'。
#
# 返回表示最终状态的字符串。
#
# 示例 1：
#
# 输入：".L.R...LR..L.."
# 输出："LL.RR.LLRRLL.."
#
# 示例 2：
#
# 输入："RR.L"
# 输出："RR.L"
# 说明：第一张多米诺骨牌没有给第二张施加额外的力。
#
# 提示：
#
#
# 0 <= N <= 10^5
# 表示多米诺骨牌状态的字符串只含有 'L'，'R'; 以及 '.';
#
# 从左向右遍历
#   遇L
#       last是R 那么就 RR.LL 或RRLL
#       last是./L 那么就 LLLLL
#   遇R
#       last是R 那么就 RRRRR
#       last是./L 那么就 ....R
#   遇.
#       last是R 那么就 RRRRR
#       last是. 那么就....
#       last是L 可能是.或者L看下一个

#  所以分析下来， 我们记住上一次L/R下标即可。然后见招拆招


#  比较有趣的是官方题解有一种手里分析的题解。。。 不过空间复杂度为o(n)， 就不实现了。

# 我们可以对每个多米诺骨牌计算净受力。
# 我们关心的受力取决于一个多米诺骨牌和最近的左侧 'R' 右侧 'L' 的距离：
# 哪边近，就受哪边力更多。

# 算法

# 从左向右扫描，我们的力每轮迭代减少 1.重置为 N 当我们遇到一个 'R' 时，所以 force[i] 比 force[j] 大当且仅当 dominoes[i] 比 dominoes[j] 离最左边的 'R' 近。

# 类似的，从右向左扫描，可以找到向左侧的力，离 L 的远近。

# 对于骨牌的结果 answer[i]，如果左右两侧力相等，答案是 '.'。否则，哪边力大答案就是哪边。
# 下面是对字符串 S = 'R.R...L' 的模拟：我们从左向右暴力得到的结果为 [7, 6, 7, 6, 5, 4, 0]，
# 从右向左扫描的结果为 [0, 0, 0, -4, -5, -6, -7]。合并之后，合力为 [7, 6, 7, 2, 0, -2, -7] 所以最近结果为 RRRR.LL。



# @lc code=start
class Solution:
    def pushDominoes(self, dominoes: str) -> str:

        lastL = -1
        lastR = -1
        ans = ''

        for i, ch in enumerate(dominoes):
            if ch == 'L':
                if lastR <= lastL:
                    # 不受lastR控制
                    ans += 'L' * (i - lastL - 1)
                else:
                    # 受到lastR控制
                    a = (i - lastR - 1) // 2
                    b = (i - lastR - 1) % 2
                    temp = 'R' * a + '.' * b + 'L' * a
                    ans += temp

                ans += 'L'
                lastL = i

            elif ch == 'R':
                if lastR > lastL:
                    # 受到lastR控制
                    ans += 'R' * (i - lastR - 1)
                else:
                    ans += '.' * (i - lastL - 1)

                ans += 'R'
                lastR = i

        if lastR > lastL:
            ans = ans + 'R' * (len(dominoes) - lastR - 1)
        else:
            ans = ans + '.' * (len(dominoes) - lastL - 1)


        return ans


    # 官方受力分析法，好好玩
    # def pushDominoes(self, dominoes):
    #     N = len(dominoes)
    #     force = [0] * N

    #     # Populate forces going from left to right
    #     f = 0
    #     for i in xrange(N):
    #         if dominoes[i] == 'R': f = N
    #         elif dominoes[i] == 'L': f = 0
    #         else: f = max(f-1, 0)
    #         force[i] += f

    #     # Populate forces going from right to left
    #     f = 0
    #     for i in xrange(N-1, -1, -1):
    #         if dominoes[i] == 'L': f = N
    #         elif dominoes[i] == 'R': f = 0
    #         else: f = max(f-1, 0)
    #         force[i] -= f

    #     return "".join('.' if f==0 else 'R' if f > 0 else 'L' for f in force)

# @lc code=end
