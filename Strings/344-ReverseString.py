from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        half_lenght = int(len(s) // 2)
        for k in range(half_lenght):
            # temp = s[k]
            # s[k] = s[len(s)-1-k]
            # s[len(s)-1-k] = temp
            s[k], s[len(s) - 1 - k] = s[len(s) - 1 - k], s[k]

    # https://leetcode.com/problems/reverse-string/solution/
    def reverseString_answer(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1


if __name__ == "__main__":
    solution = Solution()
    string1 = ["h", "e", "l", "l", "o"]
    print("before reverse:{}".format(string1))
    solution.reverseString(string1)
    print("after reverse:{}".format(string1))

    solution.reverseString_answer(string1)
    print("after reverse:{}".format(string1))
