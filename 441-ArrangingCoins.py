class Solution:
    # binary search
    # Time complexity : O(logN).
    # Space complexity : O(1).
    # https://leetcode.com/problems/arranging-coins/solution/
    def arrangeCoins(self, n: int) -> int:
        left = 0
        right = n
        while left <= right:
            k = left + (right - left) // 2
            cur = k * (k + 1) // 2
            while cur == n:
                return k
            if cur > n:
                right = k - 1
            else:
                left = k + 1
        return right

    def arrangeCoins2(self, n: int) -> int:
        return (int)((2 * n + 0.25) ** 0.5 - 0.5)
    # force brute
    def arrangeCoins3(self, n: int) -> int:
        if n <= 0:
            return 0
        rows = 1
        i = 1
        while n >= 0:
            n = n - i
            i += 1
            if n >= i:
                rows += 1

        return rows

solution = Solution()
print(solution.arrangeCoins(5))
print(solution.arrangeCoins(8))
print(solution.arrangeCoins(3))