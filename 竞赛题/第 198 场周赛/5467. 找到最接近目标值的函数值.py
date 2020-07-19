
# Winston 构造了一个如上所示的函数 func 。他有一个整数数组 arr 和一个整数 target ，他想找到让 |func(arr, l, r) - target| 最小的 l 和 r 。
# 这个func就是全部与运算
# 请你返回 |func(arr, l, r) - target| 的最小值。

# 请注意， func 的输入参数 l 和 r 需要满足 0 <= l, r < arr.length 。



# 我们从小到大遍历 r，并用一个集合维护所有的 func(arr, l, r) 的值，集合的大小小于等于 20。

# 当我们遍历到 r+1 时，新的值为原集合中的每个值和 arr[r+1] 进行按位与运算得到的结果，附带一个 arr[r+1] 本身。我们对这些新的值进行去重，就可以得到 func(arr, l, r+1) 的值。

# 对于每个值，我们更新一次答案即可。


# 注意与运算 单调递减， 同样一个数对自身的与运算等于本身 ，与运算会丢失信息，无法还原。 即没有前缀和的办法

class Solution:
    def closestToTarget(self, arr: List[int], target: int) -> int:
        ans = abs(arr[0] - target)
        valid = {arr[0]}
        for num in arr:
            valid = {x & num for x in valid} | {num}
            ans = min(ans, min(abs(x - target) for x in valid))
        return ans
