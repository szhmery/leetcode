class Solution:
    def addDigits(self, num: int) -> int:

        def helper(num):
            res = 0
            while num:
                res += num % 10
                num //= 10
            return res
        while num >= 10:
            num = helper(num)
        return num

    def addDigits_n(self, num: int) -> int:
        if num <= 9:
            return num
        tmp = 0
        while num:
            tmp += num % 10
            num //= 10
        return self.addDigits_n(num)

    # https://leetcode.com/problems/add-digits/solution/
    def addDigits2(self, num: int) -> int:
        digital_root = 0
        while num > 0:
            digital_root += num % 10
            num = num // 10

            if num == 0 and digital_root > 9:
                num = digital_root
                digital_root = 0

        return digital_root

    def addDigits3(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        return num % 9

    def addDigits4(self, num: int) -> int:
        return 1 + (num - 1) % 9 if num else 0

if __name__ == '__main__':
    solution = Solution()

    result = solution.addDigits(38)
    print(result)
