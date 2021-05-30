class Solution:
    # binary search
    def isPerfectSquare(self, num: int) -> bool:
        low = 0
        high = num
        while low <= high:
            mid = (low + high) // 2
            res = mid * mid
            if res == num:
                return True
            elif res > num:
                high = mid - 1
            else:
                low = mid + 1
        return False


if __name__ == "__main__":
    solution = Solution()
    result = solution.isPerfectSquare(8)
    print(result)
    result = solution.isPerfectSquare(16)
    print(result)

