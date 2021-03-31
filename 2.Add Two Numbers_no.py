"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
def add_two_numbers(l1, l2):
    l1 = ''.join(l1)
    l2 = ''.join(l2)
    solution = int(l1)+int(l2)
    return solution


if __name__ == "__main__":
    l1 = list(input().split())
    l2 = list(input().split())
    print(add_two_numbers(l1,l2))