from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return_digits = digits.copy()
        if digits[len(digits) - 1] + 1 == 10:
            return_digits[len(return_digits) - 1] = 0
            if len(digits) == 1:
                return_digits = [1] + return_digits
                return return_digits
            return_digits = self.plusOne(digits[:-1]) + [0]

        else:
            return_digits[len(return_digits) - 1] += 1

        return return_digits


if __name__ == "__main__":
    solution = Solution()
    before_num = [0, 1]
    print("before plus one:{}".format(before_num))
    after_num = solution.plusOne(before_num)
    print("after plus one:{}".format(after_num))

    before_num = [0, 9]
    print("before plus one:{}".format(before_num))
    after_num = solution.plusOne(before_num)
    print("after plus one:{}".format(after_num))

    before_num = [1, 2, 3, 4]
    print("before plus one:{}".format(before_num))
    after_num = solution.plusOne(before_num)
    print("after plus one:{}".format(after_num))

    before_num = [0, 0]
    print("before plus one:{}".format(before_num))
    after_num = solution.plusOne(before_num)
    print("after plus one:{}".format(after_num))

    before_num = [9, 9]
    print("before plus one:{}".format(before_num))
    after_num = solution.plusOne(before_num)
    print("after plus one:{}".format(after_num))
