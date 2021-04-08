"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

"""


# Идея: найти минимальной длины слово,
# Посимвольно каждую букву проверяем в каждом другом слове с буквой а той же позиции  в "минимальном слове",
# если не совпадает - возвращаем строку до символа, на котором остановились.
# проверить на отсутствие слов в исходном словаре иначе функция min выдаст ошибку
class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        min_word = min(strs, key=len)
        for ind, letter in enumerate(min_word):
            for other_words in strs:
                if other_words[ind] != letter:
                    return min_word[:ind]
        return min_word



if __name__ == "__main__":
    sol = Solution()
    # tests
    print(sol.longestCommonPrefix(strs=["flower","flow","flight"]))
    print(sol.longestCommonPrefix(strs=["dog","racecar","car"]))
    print(sol.longestCommonPrefix(strs=['irrras','irrtgh','irrthg']))
    print(sol.longestCommonPrefix(strs=['', 'zzz', 'kkk']))