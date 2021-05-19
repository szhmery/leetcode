from typing import List


class Solution:
    #https://www.bilibili.com/video/BV1gi4y137GW
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits
        return [1] + digits

    def plusOne2(self, digits: List[int]) -> List[int]:
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

    def plusOne2(self, digits: List[int]) -> List[int]:
        bit = 1
        for i in range(len(digits)-1, -1, -1):
            a = digits[i] + bit
            bit = a // 10
            digits[i] = a % 10
        if bit == 1:
            digits.insert(0, 1)
        return digits



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
    before_num = [9, 9]
    print("before plus one:{}".format(before_num))
    after_num = solution.plusOne2(before_num)
    print("after plus one:{}".format(after_num))