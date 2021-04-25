class Solution:
    def mySqrt(self, x: int) -> int:

        """
        :type x: int
        :rtype: int
        """
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
    result = solution.mySqrt(16)
    print(result)
    result = solution.mySqrt(6)
    print(result)
    result = solution.mySqrt(0)
    print(result)
