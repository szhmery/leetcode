
class Solution:
    # # https://www.bilibili.com/video/BV1rV411r7AL
    def isPowerOfTwo(self, n: int) -> bool:
        return n and n & (n - 1) == 0
