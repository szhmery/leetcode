class Solution:
    # https://www.bilibili.com/video/BV1Ca4y1v7Qr?from=search&seid=14593151185398909445
    # hash set
    # Time complexity : O(n)
    # Space complexity : O(n)
    def isHappy(self, n: int) -> bool:
        num_set = set()
        while n != 1:
            if n in num_set:
                return False
            num_set.add(n)
            n = self.squares(n)

        return True

    # slow fast point
    # Time complexity : O(n)
    # Space complexity : O(1)
    def isHappy(self, n: int) -> bool:
        slow = fast = n

        slow = self.squares(slow)
        fast = self.squares(fast)
        fast = self.squares(fast)

        while slow != fast:
            slow = self.squares(slow)
            fast = self.squares(fast)
            fast = self.squares(fast)

        return slow == 1

    def squares(self, num):
        ans = 0
        while num > 0:
            ans += (num % 10) ** 2
            num //= 10
        return ans


if __name__ == '__main__':
    solution = Solution()

    result = solution.isHappy(19)
    print(result)

    result = solution.isHappy(2)
    print(result)
