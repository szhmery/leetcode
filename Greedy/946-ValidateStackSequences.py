from typing import List


class Solution:
    # greedy
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        j = 0
        n = len(pushed)
        if n != len(popped) or not popped or not pushed:
            return False
        for x in pushed:
            stack.append(x)
            while stack and j < n and stack[-1] == popped[j]:
                stack.pop()
                j += 1
        return j == len(popped)

    def validateStackSequences2(self, pushed: List[int], popped: List[int]) -> bool:
        stack = []
        n = len(pushed)
        if n != len(popped):
            return False
        j = 0
        i = 0
        while i < n:
            while len(stack) == 0 or popped[i] != stack[-1]:
                if j < n:
                    stack.append(pushed[j])
                    j += 1
                else:
                    return False
            stack.pop()
            i += 1
        return not stack and j == i == n


solution = Solution()
push = [1, 2, 3, 4, 5]
pop = [4, 5, 3, 2, 1]
print(solution.validateStackSequences(push, pop))

push = [1, 2, 3, 4, 5]
pop = [4, 3, 5, 1, 2]
print(solution.validateStackSequences(push, pop))
