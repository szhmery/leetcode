from typing import List


class Solution:
    # DFS, 递归
    # 时间复杂度：O(2 ^ n)
    # 空间复杂度：O(n)

    def letterCombinations(self, digits: str) -> List[str]:
        number_mapping = [' ', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        result = []
        if digits == '':
            return result
        self.findCombination(digits, number_mapping, 0, '', result)
        return result

    def findCombination(self, digits, mapping, index, string, res):
        if index == len(digits):
            res.append(string)
            return
        num = digits[index]
        letter = mapping[int(num)]
        for i in range(len(letter)):
            self.findCombination(digits, mapping, index + 1, string + letter[i], res)
        return

    # # iterative
    # def letterCombinations2(self, digits: str) -> List[str]:
    #     result = []
    #     if digits == '':
    #         return result
    #     number_mapping = [' ', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    #     for i in len(digits):
    #         t = []
    #         string = number_mapping[int(digits[i])]
    #         for j in range(len(string)):
    #             for letter in result:
    #                 t.append(letter + string[j])
    #         result = t
    #     return result


if __name__ == '__main__':
    solution = Solution()
    result = solution.letterCombinations('29')
    print(result)
