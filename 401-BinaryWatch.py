from typing import List


class Solution:
    # https://leetcode.com/problems/binary-watch/discuss/88458/Simple-Python%2BJava
    def readBinaryWatch(self, turnedOn: int) -> List[str]:

        ans = []
        for h in range(12):
            for m in range(60):
                if (bin(h) + bin(m)).count('1') == turnedOn: # 1, 2, 4, 8, 16, 32, they all have only 1 bit on the fisrt bit
                    ans.append('%d:%02d' % (h, m))
        return ans


solution = Solution()
result = solution.readBinaryWatch(9)
print(result)

result = solution.readBinaryWatch(1)
print(result)

result = solution.readBinaryWatch(2)
print(result)
