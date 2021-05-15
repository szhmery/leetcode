class Solution:
    # https://www.bilibili.com/video/BV1ab411V7Uy?from=search&seid=2602301199667527773
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return str(0)
        ans = []
        result = ''
        remainder_dict = {}
        if (numerator > 0 and denominator < 0) or (numerator < 0 and denominator > 0):
            ans.append('-')
        divisor = abs(numerator)
        dividend = abs(denominator)
        ans.append(divisor // dividend)

        remainder = divisor % dividend
        if remainder == 0:
            for char in ans:
                result += str(char)
            return result
        ans.append('.')

        while remainder != 0:
            if remainder in remainder_dict:
                ans.insert(remainder_dict[remainder], '(')
                ans.append(")")
                break
            else:
                remainder_dict[remainder] = len(ans)
                remainder *= 10
                ans.append(remainder // dividend)
                remainder %= dividend


        for char in ans:
            result += str(char)
        return result



if __name__ == '__main__':
    solution = Solution()
    numerator = 1
    denominator = 2
    result = solution.fractionToDecimal(numerator, denominator)
    print(result)

    numerator = -2147483648
    denominator = 1
    result = solution.fractionToDecimal(numerator, denominator)
    print(result)

