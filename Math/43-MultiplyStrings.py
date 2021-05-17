class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1 = len(num1)
        n2 = len(num2)
        res = ['0'] * (n1 + n2)
        ans = ''
        for j in range(n2 - 1, -1, -1):
            for i in range(n1 - 1, -1, -1):
                product = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                tmp = ord(res[i + j + 1]) - ord('0') + product
                res[i + j + 1] = str(tmp % 10)
                res[i + j] = str((ord(res[i + j]) - ord('0')) + tmp // 10)
        if res[0] == '0':
            res = res[1:]
        for c in res:
            ans += c
        return ans if len(res) != 0 else '0'

    # https://blog.csdn.net/fuxuemingzhu/article/details/80681702
    def multiply2(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 == '0':
            return '0'
        ans = 0
        for i, n1 in enumerate(num2[::-1]):
            pre = 0
            curr = 0
            for j, n2 in enumerate(num1[::-1]):
                multi = (ord(n1) - ord('0')) * (ord(n2) - ord('0'))
                first, second = multi // 10, multi % 10
                curr += (second + pre) * (10 ** j)
                pre = first
            curr += pre * (10 ** len(num1))
            ans += curr * (10 ** i)
        return str(ans)


if __name__ == "__main__":
    solution = Solution()
    result = solution.multiply('2', '3')
    print(result)
    result = solution.multiply('2', '5')
    print(result)
    result = solution.multiply('123', '3')
    print(result)
    result = solution.multiply('999', '999')
    print(result)