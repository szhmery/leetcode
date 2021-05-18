class Solution:
    def countPrimes(self, n: int) -> int:
        isPrimes = [True for i in range(n)]
        i = 2
        while i * i < n:
            if not isPrimes[i]:
                i += 1
                continue
            for j in range(i * i, n, i):
                isPrimes[j] = False
            i += 1

        count = 0
        for i in range(2, n):
            if isPrimes[i]:
                count += 1
        return count


if __name__ == '__main__':
    solution = Solution()
    n = 5
    result = solution.countPrimes(n)
    print('give {0}, count of prime:{1}'.format(n, result))

    n = 50
    result = solution.countPrimes(n)
    print('give {0}, count of prime:{1}'.format(n, result))
