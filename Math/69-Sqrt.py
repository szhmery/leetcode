class Solution:
    # binary search
    # https://www.bilibili.com/video/BV1PK411s72g?from=search&seid=3392214132115941691
    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

    def mySqrt2(self, x: int) -> int:
        if x <= 1:
            return x

        low, high = 1, x
        while low <= high:

            mid = (low + high) // 2
            mid2 = mid ** 2
            if mid2 == x:
                return mid
            elif mid2 < x:
                low = mid + 1
            elif mid2 > x:
                high = mid - 1
        return high


if __name__ == "__main__":
    solution = Solution()
    result = solution.mySqrt(8)
    print(result)
    result = solution.mySqrt2(8)
    print(result)
    result = solution.mySqrt(16)
    print(result)
    result = solution.mySqrt2(16)
    print(result)
    result = solution.mySqrt(6)
    print(result)
    result = solution.mySqrt2(6)
    print(result)
    result = solution.mySqrt(0)
    print(result)
    result = solution.mySqrt2(0)
    print(result)
