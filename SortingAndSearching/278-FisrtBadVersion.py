# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
def isBadVersion(version):
    if version >= 3:
        return True
    else:
        return False

class Solution:
    # binary search
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left < right:
            mid = left + (right - left)//2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    solution = Solution()
    version = solution.firstBadVersion(9)

    print(version)