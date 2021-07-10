class Solution:
    # https://www.bilibili.com/video/BV1p5411a7h1
    def isPowerOfFour(self, n: int) -> bool:
        # return n > 0 and n & (n - 1) == 0 and n % 3 == 1
        if not n & (n - 1) and (n & 0x55555555):
            return True
        return False
    #check the 1 - bit location;


if __name__ == '__main__':
    solution = Solution()
    n = 16
    result = solution.isPowerOfFour(n)
    print('give {0}, count of prime:{1}'.format(n, result))
