import collections
from typing import List


class Solution:
    # Complexity Analysis
    # Time Complexity: O(NK), where NN is the length of strs, and K is the maximum length of a string in strs.
    # Counting each string is linear in the size of the string, and we count every string.
    # Space Complexity: O(NK), the total information content stored in ans.
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                count[index] += 1
            ans[tuple(count)].append(s)
        return ans.values()

    # Complexity Analysis
    # Time Complexity: O(NKlogK), where NN is the length of strs, and K is the maximum length of a string in strs.
    # The outer loop has complexity O(N) as we iterate through each string. Then, we sort each string in O(KlogK) time.
    # Space Complexity: O(NK), the total information content stored in ans.
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        ans = collections.defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()




if __name__ == '__main__':
    solution = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = solution.groupAnagrams2(strs)
    print(result)
