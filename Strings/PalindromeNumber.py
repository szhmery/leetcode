class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted_number = 0
        while x > reverted_number:
            reverted_number = reverted_number * 10 + x % 10
            x = int(x / 10)

        return x == reverted_number or x == int(reverted_number / 10)


if __name__ == '__main__':
    solution = Solution()
    x = 12321
    result = solution.isPalindrome(x)
    print("before reverse:{}".format(x))
    print("after reverse:{}".format(result))
