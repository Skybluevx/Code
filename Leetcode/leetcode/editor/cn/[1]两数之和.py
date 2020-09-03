# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。 
# 
#  你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。 
# 
#  
# 
#  示例: 
# 
#  给定 nums = [2, 7, 11, 15], target = 9
# 
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
#  
#  Related Topics 数组 哈希表 
#  👍 9030 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# 方法1
# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         for i, num in enumerate(nums):
#             if (target - num) in nums[i+1:]:
#                 return [i, nums[i+1:].index((target - num)) + (len(nums) - len(nums[i+1:]))]

# 方法2
class Solution(object):
    def twoSum(self, nums, target):
        nums_dict = {}
        for a, num in enumerate(nums):
            nums_dict[num] = a
        for i, num in enumerate(nums):
            j = nums_dict.get(target - num)
            if j is not None and j != i:
                return [i, j]
# leetcode submit region end(Prohibit modification and deletion)

so = Solution()
print(so.twoSum([3, 3], 6))
