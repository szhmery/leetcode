import math

class Solution:
    # https://www.bilibili.com/video/BV11Q4y1N7YS?from=search&seid=13912497943117414274
    def countPrimes(self, n: int) -> int:
        isPrimes = [True] * n
        isPrimes[0] = isPrimes[1] = False
        i = 2
        while i * i < n:
            if isPrimes[i]:
                for j in range(i * i, n, i):
                    isPrimes[j] = False
            i += 1

        return sum(isPrimes)

    def countPrimes2(self, n: int) -> int:
        if n <= 2:
            return 0

        numbers = {}
        for p in range(2, int(math.sqrt(n)) + 1):
            if p not in numbers:
                for multiple in range(p * p, n, p):
                    numbers[multiple] = 1

        # Exclude "1" and the number "n" itself.
        return n - len(numbers) - 2


if __name__ == '__main__':
    solution = Solution()
    n = 5
    result = solution.countPrimes(n)
    print('give {0}, count of prime:{1}'.format(n, result))
    result = solution.countPrimes2(n)
    print('give {0}, method 2 count of prime:{1}'.format(n, result))

    n = 50
    result = solution.countPrimes(n)
    print('give {0}, count of prime:{1}'.format(n, result))
    result = solution.countPrimes2(n)
    print('give {0}, method 2 count of prime:{1}'.format(n, result))
