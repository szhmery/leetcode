
class Solution:
    # # https://www.bilibili.com/video/BV1rV411r7AL
    def isPowerOfTwo(self, n: int) -> bool:
        # return n > 0 and n & (n - 1) == 0
        return n > 0 and (n & -n) == n  # this is faster than the first one, no minus operation