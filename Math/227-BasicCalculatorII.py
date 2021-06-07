class Solution:
    def calculate(self, s: str) -> int:
        def is_digit(char):
            if ord('0') <= ord(char) <= ord('9'):
                return True
            else:
                return False

        n = len(s)
        if n == 0:
            return 0
        stack = []
        curr = 0
        operation = '+'
        for i in range(n):
            char = s[i]
            if is_digit(char):
                curr = curr * 10 + int(char)
            if not is_digit(char) and char != ' ' or i == n - 1:
                if operation == '+':
                    stack.append(curr)
                elif operation == '-':
                    stack.append(-curr)
                elif operation == '*':
                    value = stack.pop()
                    stack.append(value * curr)
                elif operation == '/':
                    value = stack.pop()
                    stack.append(int(value / curr))
                operation = char
                curr = 0

        res = 0
        while stack:
            res += stack.pop()
            # stack.pop()
        return res

    def calculate2(self, s: str) -> int:

        n = len(s)
        if n == 0:
            return 0
        result = 0
        curr = 0
        last_number = 0
        operation = '+'
        for i in range(n):
            char = s[i]
            if char.isdigit():
                curr = curr * 10 + int(char)

            if not char.isdigit() and char != ' ' or i == n - 1:
                if operation == '+':
                    result += last_number
                    last_number = curr
                elif operation == '-':
                    result += last_number
                    last_number = -curr
                elif operation == '*':
                    last_number = last_number * curr
                elif operation == '/':
                    last_number = int(last_number / curr)
                operation = char
                curr = 0
        result += last_number
        return result


if __name__ == '__main__':
    solution = Solution()
    s = "3+2*2"
    result = solution.calculate(s)
    print(result)
    result = solution.calculate2(s)
    print(result)

    s="14-3/2"
    result = solution.calculate(s)
    print(result)
    result = solution.calculate2(s)
    print(result)


