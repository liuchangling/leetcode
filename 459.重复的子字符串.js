/*
 * @lc app=leetcode.cn id=459 lang=javascript
 *
 * [459] 重复的子字符串
 *
 * https://leetcode-cn.com/problems/repeated-substring-pattern/description/
 *
 * algorithms
 * Easy (47.81%)
 * Likes:    325
 * Dislikes: 0
 * Total Accepted:    44.2K
 * Total Submissions: 86.5K
 * Testcase Example:  '"abab"'
 *
 * 给定一个非空的字符串，判断它是否可以由它的一个子串重复多次构成。给定的字符串只含有小写英文字母，并且长度不超过10000。
 * 
 * 示例 1:
 * 
 * 
 * 输入: "abab"
 * 
 * 输出: True
 * 
 * 解释: 可由子字符串 "ab" 重复两次构成。
 * 
 * 
 * 示例 2:
 * 
 * 
 * 输入: "aba"
 * 
 * 输出: False
 * 
 * 
 * 示例 3:
 * 
 * 
 * 输入: "abcabcabcabc"
 * 
 * 输出: True
 * 
 * 解释: 可由子字符串 "abc" 重复四次构成。 (或者子字符串 "abcabc" 重复两次构成。)
 * 
 * 
 */

// 思路1  分为n份 如果每份都一样就返回true 直到n = length  61.96 % 92ms
// 思路2  我们将两个 s 连在一起，并移除第一个和最后一个字符。
// 如果 s 是该字符串的子串，那么 s 就满足题目要求。
// 原因： 如果长度为 n 的字符串 s 是字符串 t=s+s的子串，
// 并且 s 在 t 中的起始位置不为 0 或 n，那么 s 就满足题目的要求
// 正确性证明在官方题解里面 有点帅的。


// @lc code=start
// 方法1
// var check = function (s, i){
//     step = s.length / i ;
//     const start = s.substr(0, step)
//     for(let j = 1 ; j < i ; j ++){
//         let temp = s.substr(j * step, step)
//         if(temp != start) return false
//     }
//     return true;    
// }

// /**
//  * @param {string} s
//  * @return {boolean}
//  */
// var repeatedSubstringPattern = function(s) {
//     l = s.length;
//     for(let i = 2; i <= l; i ++){
//         if (l % i == 0 ){
//             if(check(s, i)){
//                 return true;
//             }
//         }
//     }
//     return false;
// };



// 方法2 67.48% 88ms
var repeatedSubstringPattern = function(s) {
    let idx = (s+s).substring(1, 2*s.length-1).indexOf(s)
    return idx != s.length && ~idx
}

// TODO KMP...

// @lc code=end

// console.log(repeatedSubstringPattern("aba"))
