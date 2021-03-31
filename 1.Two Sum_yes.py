"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


class Solution:
    def twoSum(self, nums, target):
        for i in enumerate(nums):
            if target - i[1] in nums[i[0] + 1:]:
                return i[0], nums[i[0] + 1:].index(target - i[1]) + i[0] + 1


if __name__ == "__main__":
    sol = Solution()
    #tests
    print(sol.twoSum(nums=[2, 7, 11, 15, -3], target=9))
    print(sol.twoSum(nums=[3, 2, 4], target=6))
    print(sol.twoSum(nums=[3, 3], target=6))
