"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
"""


# Идея: написать "стек"
# Создать словарь с парами значений со скобками,
# Пройтись по строке, если символ - "открывающаяся скобка", добавляем в массив,
# Если нет (закрывающаяся) - сравнить со значением полученным по последнему ключу из стека. Если совпали - убераем ключ, очищаем стек.
# Если не совпали возвращаем false
# Если размер стека в итоге = 0 - возвращаем true

class Solution:
    def isValid(self, s: str):
        dict_brackets = {'(': ')', '[': ']', '{': '}'}
        stack = []
        if len(s) == 0:
            return False
        for bracket in s:
            # открывающаяся скобка
            if bracket in dict_brackets.keys():
                stack.append(bracket)
            if bracket in dict_brackets.values():
                # закрывающаяся скобка совпадающая со значением по ключу своей "открывающейся пары"
                if len(stack) > 0 and dict_brackets.get(stack[-1]) == bracket:
                    stack.pop(len(stack) - 1)
                else:
                    return False
        return len(stack) == 0


if __name__ == "__main__":
    sol = Solution()
    # tests
    print(sol.isValid(s="()[]{}"))
    print(sol.isValid(s="(((]["))
    print(sol.isValid(s="()[]}}"))
    print(sol.isValid(s="{{[(("))
    print(sol.isValid(s="{[()]}"))
    print(sol.isValid(s=""))
