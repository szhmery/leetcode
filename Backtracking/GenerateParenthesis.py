from typing import List


class Solution:
    # https://www.dazhuanlan.com/2019/11/30/5de1569c1fe19/
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        if n <= 0:
            return result
        self.helper(result, '', n, n)
        return result

    def helper(self, result: List, string, left_number, right_number):
        if left_number == right_number == 0:
            result.append(string)
            return result
        if left_number > 0:
            self.helper(result, string + '(', left_number - 1, right_number)
        if left_number < right_number:
            self.helper(result, string + ')', left_number, right_number - 1)


if __name__ == '__main__':
    solution = Solution()
    n = 3
    result = solution.generateParenthesis(3)
    print(result)
