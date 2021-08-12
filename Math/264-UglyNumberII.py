import heapq
class Solution:
    # DP
    # time complexity O(n)
    # space complexity O(n)
    #https://leetcode.com/problems/ugly-number-ii/discuss/69364/My-16ms-C%2B%2B-DP-solution-with-short-explanation
    def nthUglyNumber(self, n: int) -> int:
        if n <= 0:
            return 0
        if n == 1:
            return 1
        dp = [0] * n
        dp[0] = 1
        #表示下一个丑数是当前指针指向的丑数乘以对应的质因数
        t2, t3, t5 = 0, 0, 0
        for i in range(1, n):
            dp[i] = min(dp[t2] * 2, dp[t3] * 3, dp[t5] * 5)
            if dp[i] == dp[t2] * 2:  # t2是首个乘以2大于dp[i]的丑数的index，同理t3,t5
                t2 += 1
            if dp[i] == dp[t3] * 3: # 如果多个if条件都满足，说明这个也是最新丑数的因子，都需要+1.
                t3 += 1
            if dp[i] == dp[t5] * 5:
                t5 += 1
        return dp[n - 1]
    #headp
    # time complexity O(nlogn)
    # space complexity O(n)
    def nthUglyNumber2(self, n):
        seen = {1}
        heap = [1]
        factors = [2,3,5]
        for i in range(1, n):
            cur = heapq.heappop(heap) # pop up the smallest number
            for factor in factors: # use this number to multiply 2,3,5. Save the results into seen and push them to the heap
                next = cur * factor
                if next not in seen:
                    seen.add(next)
                    heapq.heappush(heap, next)
        return heapq.heappop(heap)

    # use heapq
    def nthUglyNumber3(self, n):
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        while n > 1:
            u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
            umin = min((u2, u3, u5))
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1
            ugly.append(umin)
            n -= 1
        return ugly[-1]

    def nthUglyNumber4(self, n: int) -> int:
        def isUglyNumber(n: int) -> bool:
            if n == 0 :
                return False
            while n % 2 == 0:
                if n in seen:
                    return True
                n //= 2
            while n % 3 == 0:
                if n in seen:
                    return True
                n //= 3
            while n % 5 == 0:
                if n in seen:
                    return True
                n //= 5
            return n == 1
        index = 0
        seen = set()
        num = 1
        mx = 0
        while index < n:
            if isUglyNumber(num):
                mx = num
                seen.add(num)
                index += 1
            num += 1

        return mx

solution = Solution()
print(solution.nthUglyNumber(10))
print(solution.nthUglyNumber2(10))