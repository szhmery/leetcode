class Solution:
    def isValid(self, s):
        stack = []
        bracket_map = {"}": "{", "]": "[", ")": "("}
        for char in s:
            if char in bracket_map.keys():
                if stack:
                    if stack.pop() != bracket_map[char]:
                        return False
                else:
                    return False
            else:
                stack.append(char)
        return not stack

    def isValid2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # method 1
        stack = []
        top_element = ''
        bracket_map = {"}": "{", "]": "[", ")": "("}
        for char in s:
            if char in bracket_map:
                if stack:
                    top_element = stack.pop()
                else:
                    '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)
        return not stack


if __name__ == '__main__':
    solution = Solution()
    s = "()[]{}"
    result = solution.isValid(s)
    print(result)
    s = "(]"
    result = solution.isValid(s)
    print(result)
