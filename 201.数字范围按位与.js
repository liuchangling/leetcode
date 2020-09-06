/*
 * @lc app=leetcode.cn id=201 lang=javascript
 *
 * [201] 数字范围按位与
 *
 * https://leetcode-cn.com/problems/bitwise-and-of-numbers-range/description/
 *
 * algorithms
 * Medium (44.95%)
 * Likes:    196
 * Dislikes: 0
 * Total Accepted:    28.8K
 * Total Submissions: 57.7K
 * Testcase Example:  '5\n7'
 *
 * 给定范围 [m, n]，其中 0 <= m <= n <= 2147483647，返回此范围内所有数字的按位与（包含 m, n 两端点）。
 * 
 * 示例 1: 
 * 
 * 输入: [5,7]
 * 输出: 4
 * 
 * 示例 2:
 * 
 * 输入: [0,1]
 * 输出: 0
 * 
 */


// 方法1 62% 找寻m和n的公共最长前缀
// 方法2 72% Brian Kernighan 算法
// 关键在于我们每次对 n 和 n−1 之间进行按位与运算后，
// number 中最右边的 1 会被抹去变成 0.
// 一直n & n-1 直到n<m。 其实这道题思路很明显从大到小计算比较快，该算法很精简了


// @lc code=start
/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
// 方法1 62%
// var rangeBitwiseAnd = function(m, n) {
//     let shift = 0
//     while(m < n){
//         shift++;
//         m >>= 1
//         n >>= 1
//     }
//     return m << shift
// };

// 方法2 72%
var rangeBitwiseAnd = function(m, n) {
    while(m < n){
        n = n & (n-1)
    }
    return n
};
// @lc code=end

