class Solution:
    # https://leetcode.com/problems/count-and-say/discuss/1207074/C%2B%2B-or-Faster-than-100
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        return self.say(self.countAndSay(n - 1))

    def say(self, number):
        count = 1
        return_str = ''

        for i in range(len(number)):
            if i == len(number) - 1 or number[i] != number[i+1]:
                return_str += str(count) + number[i]
                count = 0
            count += 1
        return return_str

    def countAndSay2(self, n):
        """
        :type n: int
        :rtype: str
        """
        return ''.join(self.nextSequence(n, ['1', 'E']))

    def nextSequence(self, n, prevSeq):
        if n == 1:
            return prevSeq[:-1]

        nextSeq = []
        prevDigit = prevSeq[0]
        digitCnt = 1
        for digit in prevSeq[1:]:
            if digit == prevDigit:
                digitCnt += 1
            else:
                # the end of a sub-sequence
                nextSeq.extend([str(digitCnt), prevDigit])
                prevDigit = digit
                digitCnt = 1

        # add a delimiter for the next sequence
        nextSeq.append('E')
        return self.nextSequence(n - 1, nextSeq)


if __name__ == '__main__':
    solution = Solution()
    print(solution.countAndSay(1))
    print(solution.countAndSay(4))
    print(solution.countAndSay(5))
    print(solution.countAndSay(10))


    print(solution.countAndSay2(1))
    print(solution.countAndSay2(4))
    print(solution.countAndSay2(5))
    print(solution.countAndSay2(10))
