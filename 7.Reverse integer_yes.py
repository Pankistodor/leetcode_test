"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned)
"""


class Solution:
    def reverse(self, x):
        string_x = str(x).strip()
        if x >= 0:
            result = int(string_x[::-1])
        else:
            result = 0 - int(string_x[:0:-1])
        if result < -2 ** 31 or result > 2 ** 31 - 1:
            return 0
        else:
            return result


if __name__ == "__main__":
    sol = Solution()
    # tests
    print(sol.reverse(x=123))
    print(sol.reverse(x=-123))
    print(sol.reverse(x=-0))
    print(sol.reverse(x=-1534236469))
