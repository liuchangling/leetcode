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



# @lc code=start
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 初始化直接用中位数搞起
        c1 = (len(nums1) -1 ) >> 1 
        c2 = (len(nums2) -1 ) >> 1 
        obj1 = self.cutArray(nums1, c1)
        obj2 = self.cutArray(nums2, c2)
        k = min(len(nums1), len(nums2))

        while obj1["notEnd"] and obj2["notEnd"] and (obj1["LVal"] > obj2["RVal"] or obj2["LVal"] > obj1["RVal"]):
            k = k >> 2
            if obj1["LVal"] > obj2["RVal"]:
                # 说明数组1的左边多了点儿
                # c1 左移k/2 c2 右移k/2
                c1 = c1 - k 
                c2 = c2 + k
            elif obj2["LVal"] > obj1["RVal"]:
                # 说明数组2的左边多了点儿
                # c2 左移k/2 c1 右移k/2
                c1 = c1 + k 
                c2 = c2 - k

            obj1 = self.cutArray(nums1, c1)
            obj2 = self.cutArray(nums2, c2)

        # print('done')
        
        mid = []
        if len(nums1) == 0:
            pass
        elif len(nums1) % 2 == 1:
            mid.append(nums1[obj1["LIndex"]])
        else :
            mid.append(nums1[obj1["LIndex"]])
            mid.append(nums1[obj1["RIndex"]])

        if len(nums2) == 0:
            pass
        elif len(nums2) % 2 == 1:
            mid.append(nums2[obj2["LIndex"]])
        else :
            mid.append(nums2[obj2["LIndex"]])
            mid.append(nums2[obj2["RIndex"]])

        mid.sort()
        print(mid)
        
       
        if len(mid) %2 == 1:
            answer =  mid[len(mid) >> 1]
        else:
            i = (len(mid) -1) >> 1
            answer = (mid[i] + mid[i+1]) /2
        
        print(answer)
        return answer

    

    def cutArray(self, array: List[int], location:int) :
        print(array, location)
        length = len(array)
        
        # 左切即为location
        LIndex = location
        LVal = None if LIndex - 1 < 0 else array[LIndex - 1]
        # array长度为奇数时,RIndex 为location;偶数时 RIndex为location +1
        RIndex = location if length % 2 == 1 else location + 1
        RVal = None if RIndex + 1 >= length else array[RIndex + 1]
        notEnd = not (LVal is None or RVal is None)

        return {
            "LIndex" : LIndex,
            "RIndex" : RIndex,
            "LVal" : LVal,
            "RVal" : RVal,
            "notEnd" : notEnd
        }

# todo fix 这种边界情况。。。
Solution().findMedianSortedArrays([1], [2,3,4])
        
# @lc code=end

