class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return str(1)
        if n > 1:
            number = self.countAndSay(n - 1)
            num_string = number
            length = len(num_string)
            count = 1
            num = num_string[0]
            return_str = ''
            if length == 1:
                return str(count) + num
            else:
                for i in range(1, len(num_string)):
                    if num_string[i] == num:
                        count += 1
                        continue
                    else:
                        return_str += str(count) + num
                        num = num_string[i]
                        count = 1
                return_str += str(count) + num
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
