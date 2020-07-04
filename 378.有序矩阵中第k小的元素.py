#
# @lc app=leetcode.cn id=378 lang=python3
#
# [378] 有序矩阵中第K小的元素
#
# https://leetcode-cn.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
#
# algorithms
# Medium (59.19%)
# Likes:    332
# Dislikes: 0
# Total Accepted:    40.1K
# Total Submissions: 64.7K
# Testcase Example:  '[[1,5,9],[10,11,13],[12,13,15]]\n8'
#
# 给定一个 n x n 矩阵，其中每行和每列元素均按升序排序，找到矩阵中第 k 小的元素。
# 请注意，它是排序后的第 k 小元素，而不是第 k 个不同的元素。
# 
# 
# 
# 示例：
# 
# matrix = [
# ⁠  [ 1,  5,  9],
# ⁠  [10, 11, 13],
# ⁠  [12, 13, 15]
# ],
# k = 8,
# 
# 返回 13。
# 
# 
# 
# 
# 提示：
# 你可以假设 k 的值永远是有效的，1 ≤ k ≤ n^2 。
# 
# 思路1 暴力 216ms
# 思路2 归并
# 归并排序思想的运用：普通归并排序是两个有序数组合并，这道题相当于N个有序数组合并，因此需要N个指针，归并到第K个元素就退出
# 思路3 二分查找 200ms 96%
# 这个思路简直了，首先知道最小值和最大值。直接进行二分查找，猜测答案为mid
# 对于mid 我们的操作是。从左下角开始，找有多少个小于mid的数。 根据个数和k是否match得出结论即可
# 怎么找呢有多少个小于mid呢？ 左下角起开始遍历
# 如果当前数小于等于mid，则加一列，即加上方的所有和当前值  += i+1。然后向右移动
# 如果当前数大于mid 就直接上一一行，完事~

# @lc code=start
class Solution:
    # 思路1 排序后输出，216ms 74% 时间 n^2 * logn 空间 n^2    
    # def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # size = len(matrix)
        # nums = matrix[0]
        # for i in range(1, size):
        #     temp = matrix[i]
        #     nums.extend(temp)
        # nums.sort()
        # return nums[k-1]

    # 思路2 归并排序 时间klogn 空间n 256ms 50%
    # def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
    #     n = len(matrix)
    #     pq = [(matrix[i][0], i, 0) for i in range(n)]
    #     heapq.heapify(pq)

    #     ret = 0
    #     for i in range(k - 1):
    #         num, x, y = heapq.heappop(pq)
    #         if y != n - 1:
    #             heapq.heappush(pq, (matrix[x][y + 1], x, y + 1))
        
    #     return heapq.heappop(pq)[0]

    # 思路3 二分查找 200ms 96%
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        def check(mid):
            i, j = n - 1, 0
            num = 0
            while i >= 0 and j < n:
                if matrix[i][j] <= mid:
                    num += i + 1
                    j += 1
                else:
                    i -= 1
            return num >= k

        left, right = matrix[0][0], matrix[-1][-1]
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        
        return left

        
# @lc code=end

