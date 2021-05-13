from typing import List


class Solution:
    # https://www.bilibili.com/video/BV16B4y1P7Nx?from=search&seid=8051840096811604789
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token == '+':
                right = stack.pop()
                left = stack.pop()
                stack.append(left + right)
            elif token == '-':
                right = stack.pop()
                left = stack.pop()
                stack.append(left - right)
            elif token == '*':
                right = stack.pop()
                left = stack.pop()
                stack.append(left * right)
            elif token == '/':
                right = stack.pop()
                left = stack.pop()
                if left * right < 0:
                    stack.append(0 - abs(left) // abs(right))
                else:
                    stack.append(left // right)
            else:
                stack.append(int(token))

        return stack.pop()


if __name__ == '__main__':
    solution = Solution()
    # tokens = ["2", "1", "+", "3", "*"]
    # result = solution.evalRPN(tokens)
    # print(result)
    #
    # tokens = ["4", "13", "5", "/", "+"]
    # result = solution.evalRPN(tokens)
    # print(result)

    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    result = solution.evalRPN(tokens)
    print(result)