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
    #时间复杂度：O(logn)，其中 n 是给定版本的数量。
    #空间复杂度：O(1)。我们只需要常数的空间保存若干变量。
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left < right: # don't add =
            mid = left + (right - left)//2
            if isBadVersion(mid):
                right = mid # 答案在区间 [left, mid] 中, don't use mid - 1, may skip the false version
            else:
                left = mid + 1
        # 此时有 left == right，区间缩为一个点，即为答案
        return left

    def firstBadVersion2(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        while left <= right:
            mid = left + (right - left)//2
            if isBadVersion(mid):
                right = mid - 1
            else:
                left = mid + 1
        # 此时有 left == right，区间缩为一个点，即为答案
        return left



if __name__ == '__main__':
    solution = Solution()
    version = solution.firstBadVersion(9)

    print(version)