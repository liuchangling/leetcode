# 面试题 16.18. 模式匹配
# 你有两个字符串，即pattern和value。 pattern字符串由字母"a"和"b"组成，用于描述字符串中的模式。例如，字符串"catcatgocatgo"匹配模式"aabab"（其中"cat"是"a"，"go"是"b"），该字符串也匹配像"a"、"ab"和"b"这样的模式。但需注意"a"和"b"不能同时表示相同的字符串。编写一个方法判断value字符串是否匹配pattern字符串。

# 示例 1：

# 输入： pattern = "abba", value = "dogcatcatdog"
# 输出： true
# 示例 2：

# 输入： pattern = "abba", value = "dogcatcatfish"
# 输出： false
# 示例 3：

# 输入： pattern = "aaaa", value = "dogcatcatdog"
# 输出： false
# 示例 4：

# 输入： pattern = "abba", value = "dogdogdogdog"
# 输出： true
# 解释： "a"="dogdog",b=""，反之也符合规则
# 提示：

# 0 <= len(pattern) <= 1000
# 0 <= len(value) <= 1000
# 你可以假设pattern只包含字母"a"和"b"，value仅包含小写字母。


# 这个题思路很简答，就是遍历a的所有可能可能长度，推算b的长度，再看是否match
# 据说难点在很多边界情况，然而我不想实现了。。。

class Solution:
    def patternMatching(self, pattern: str, value: str) -> bool:
        count_a = sum(1 for ch in pattern if ch == 'a')
        count_b = len(pattern) - count_a
        if count_a < count_b:
            count_a, count_b = count_b, count_a
            pattern = ''.join('a' if ch == 'b' else 'b' for ch in pattern)
        
        if not value:
            return count_b == 0
        if not pattern:
            return False
        
        for len_a in range(len(value) // count_a + 1):
            rest = len(value) - count_a * len_a
            if (count_b == 0 and rest == 0) or (count_b != 0 and rest % count_b == 0):
                len_b = 0 if count_b == 0 else rest // count_b
                pos, correct = 0, True
                value_a, value_b = None, None
                for ch in pattern:
                    if ch == 'a':
                        sub = value[pos:pos+len_a]
                        if not value_a:
                            value_a = sub
                        elif value_a != sub:
                            correct = False
                            break
                        pos += len_a
                    else:
                        sub = value[pos:pos+len_b]
                        if not value_b:
                            value_b = sub
                        elif value_b != sub:
                            correct = False
                            break
                        pos += len_b
                if correct and value_a != value_b:
                    return True
        
        return False
