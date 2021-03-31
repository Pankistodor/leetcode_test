"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        first_part = str(x)[:(len(str(x))) // 2:1]
        second_part = str(x)[:(len(str(x)) - 1) // 2:-1]
        if first_part == second_part:
            return True
        else:
            return False


if __name__ == "__main__":
    sol = Solution()
    # tests
    print(sol.isPalindrome(x=121))
    print(sol.isPalindrome(x=-121))
    print(sol.isPalindrome(x=10))
    print(sol.isPalindrome(x=-101))
