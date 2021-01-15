# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。 
# 
#  示例 1: 
# 
#  输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#  
# 
#  示例 2: 
# 
#  输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#  
# 
#  示例 3: 
# 
#  输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#  
#  Related Topics 哈希表 双指针 字符串 Sliding Window 
#  👍 4246 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        value = ""
        num = -1
        for i in s:
            if len(s) == 1:
                return 1
            if i not in value:
                value += i
            if s[0] == i:
                num += 1
        if num:
            return len(value)
        else:
            return len(value) - 1
# leetcode submit region end(Prohibit modification and deletion)

so = Solution()
q = so.lengthOfLongestSubstring("abcabcbb")
print(q)
