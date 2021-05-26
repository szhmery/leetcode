from typing import List


class Solution:
    # https://www.bilibili.com/video/BV1tD4y1m76j
    # Complexity Analysis
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def fizzBuzz(self, n: int) -> List[str]:
        result = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                result.append("FizzBuzz")
            elif i % 3 == 0:
                result.append("Fizz")
            elif i % 5 == 0:
                result.append("Buzz")
            else:
                result.append(str(i))
        return result

    # Complexity Analysis
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def fizzBuzz2(self, n: int) -> List[str]:
        result = []

        for i in range(1, n + 1):
            str_append = ''
            if i % 3 == 0:
                str_append += "Fizz"
            if i % 5 == 0:
                str_append += "Buzz"
            if not str_append:
                str_append = str(i)
            result.append(str_append)
        return result

    # Complexity Analysis
    # Time Complexity: O(N)
    # Space Complexity: O(1)
    def fizzBuzz3(self, n: int) -> List[str]:
        result = []
        mapping_dict = {3: 'Fizz', 5: 'Buzz'}
        for i in range(1, n + 1):
            str_append = ''
            for key in mapping_dict.keys():
                if i % key == 0:
                    str_append += mapping_dict[key]

            if not str_append:
                str_append = str(i)
            result.append(str_append)
        return result


if __name__ == '__main__':
    solution = Solution()
    n = 5
    print(n)
    result = solution.fizzBuzz2(n)
    print(result)

    n = 15
    print(n)
    result = solution.fizzBuzz2(n)
    print(result)

    n = 5
    print(n)
    result = solution.fizzBuzz3(n)
    print(result)

    n = 15
    print(n)
    result = solution.fizzBuzz3(n)
    print(result)
