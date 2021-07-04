from functools import reduce
class Solution:
    # stack
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)

    # two pointers
    def removeDuplicates_twopointers(self, s: str) -> str:
        n = len(s)
        i = 0
        s = list(s)
        for j in range(n):
            s[i] = s[j]
            if i > 0 and s[i - 1] == s[i]:
                i -= 2
            i += 1
        return ''.join(s[:i])

    def removeDuplicates3(self, S):
        return reduce(lambda s, c: s[:-1] if s[-1:] == c else s + c, S)

if __name__ == "__main__":
    solution = Solution()
    s = "abbaca"
    result = solution.removeDuplicates_twopointers(s)
    print(result)
    s = "azxxzy"
    result = solution.removeDuplicates_twopointers(s)
    print(result)
