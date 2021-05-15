from typing import List


class Compare(str):
    def __lt__(x, y):
        return x + y < y + x


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        largest_num = ''.join(sorted(map(str, nums), key=Compare, reverse=True))
        return '0' if largest_num[0] == '0' else largest_num


if __name__ == "__main__":
    solution = Solution()
    nums = [3, 30, 34, 5, 9]
    result = solution.largestNumber(nums)
    print(result)
