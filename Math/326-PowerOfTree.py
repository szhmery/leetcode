import math


class Solution:
    # Complexity Analysis
    # Time complexity : O(log_b(n).
    # In our case that is O(log3n). The number of divisions is given by that logarithm.
    # Space complexity : O(1). We are not using any additional memory.

    def isPowerOfThree2(self, n: int) -> bool:
        if n < 1:
            return False
        while n % 3 == 0:
            n = n/3
        return n == 1


if __name__ == '__main__':
    solution = Solution()
    n = 27
    result = solution.isPowerOfThree2(n)
    print('give {0}, count of prime:{1}'.format(n, result))