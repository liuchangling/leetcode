#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个有序数组的中位数
# 方法1: 从头一次遍历访问查找第 (m+n)/ 2 的数 ， 时间为 O((m+n)/2)
# 方法2：二分查找数组1和2
#       c1 c2 作为切割1，2的线
#       最终结果要求  L1 c1 R1; L2 c2 R2 当c1 和 c2 混到一起时满足：
#           -  L1 < R2 && L2 < R1 做这个，只需要检查大小即可。
#           -  L1 + L2的个数 和 R1 + R2个数相等。 满足这一点只需要偏移时，另一个数组等量反向移动即可
#       移动方式, 哪多了就缩小，哪少了就扩大。
#       二分查找步长直接从1,2中较短数组的长度不断右移一位， 直至为0
# 方法2改进，为了避免考虑过多的边界情况，这里采用一个特殊技巧
# 将1 m 视为虚拟2m+1
# 将2 n 视为虚拟2n+1
#  ～ 1 ～ 2 ～ 3 ～  => cut 2
#  ～ 1 ～ 2 ～ 3 ～ 4 ～ => cut 2&3中间的～


# @lc code=start
from typing import List

import sys
maxN = sys.maxsize


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len1 = len(nums1)
        len2 = len(nums2)

        # 保证len1较小
        if len1 > len2:
            return self.findMedianSortedArrays(nums2, nums1)
        
        low = 0 
        high = 2 * len1 # 神一般的思路，虚拟#解决奇偶坑爹边界问题

        while low <= high:
            c1 = (low + high) >> 1
            c2 = len1 + len2 - c1

            lMax1 = nums1[(c1-1)>>1] if c1 != 0 else -maxN
            rMin1 = nums1[c1>>1] if c1 != 2 * len1 else maxN

            lMax2 = nums2[(c2-1)>>1] if c2 != 0 else -maxN
            rMin2 = nums2[c2>>1] if c2 != 2 * len2 else maxN

            if lMax1 > rMin2:
                high = c1 - 1
            elif lMax2 > rMin1:
                low = c1 + 1
            else:
                break

        return (max(lMax1, lMax2) + min(rMin1, rMin2))/2

        

# print(Solution().findMedianSortedArrays([2], [1, 3, 4, 5]))

# @lc code=end
