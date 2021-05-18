from typing import List
import sys


class Solution:
    # Vertical scanning
    # Time complexity : O(S)
    # Space complexity : O(1)
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return ''
        for i in range(len(strs[0])):
            c = strs[0][i]
            for j in range(1, len(strs)):
                if i == len(strs[j]) or c != strs[j][i]:
                    return strs[0][0:i]
        return strs[0]

    # Divide and conquer
    # Time complexity : O(S)
    # Space complexity : O(m⋅logn)
    def longestCommonPrefix2(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return ''
        return self.helper(strs, 0, len(strs)-1)

    def helper(self, strs, left, right):
        if left == right:
            return strs[left]
        else:
            mid = (left + right) // 2
            lcp_left = self.helper(strs, left, mid)
            lcp_right = self.helper(strs, mid + 1, right)
            return self.commonPrefix(lcp_left, lcp_right)

    def commonPrefix(self, left_string, right_string):
        min_len = min(len(left_string), len(right_string))
        for i in range(min_len):
            if left_string[i] != right_string[i]:
                return left_string[0:i]
        return left_string[0:min_len]

    # binary search
    # Time complexity :  O(S⋅logm)
    # Space complexity : O(1)
    def longestCommonPrefix3(self, strs: List[str]) -> str:
        if strs is None or len(strs) == 0:
            return ''
        min_len = sys.maxsize
        for str in strs:
            min_len = min(min_len, len(str))
        left = 1
        right = min_len

        while left <= right:
            mid = (left + right) // 2
            if self.isCommonPrefix(strs, mid):
                left = mid + 1
            else:
                right = mid - 1
        return strs[0][0:(left + right)//2]

    def isCommonPrefix(self, strs, length):
        str1 = strs[0][0:length]
        for i in range(1, len(strs)):
            if strs[i][0:length] != str1:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    strs = ["flower", "flow", "flight"]
    result = solution.longestCommonPrefix(strs)
    print(result)
    strs = ["flower", "flow", "flight"]
    result = solution.longestCommonPrefix2(strs)
    print(result)
    strs = ["flower", "flow", "flight"]
    result = solution.longestCommonPrefix3(strs)
    print(result)