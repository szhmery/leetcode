from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        if len(strs) == 1:
            return strs[0]

        length = len(strs[0])
        for str in strs:
            length = min(len(str), length)
        if length == 0:
            return ''
        else:
            common_prefix = ''

            for i in range(length):
                tmp = strs[0][i]
                for str in strs:
                    if str[i] == tmp:
                        continue
                    else:
                        return common_prefix
                common_prefix += tmp
            return common_prefix


if __name__ == '__main__':
    solution = Solution()
    strs = ["flower", "flow", "flight"]
    print(solution.longestCommonPrefix(strs))
    strs = ["dog", "racecar", "car"]
    print(solution.longestCommonPrefix(strs))
