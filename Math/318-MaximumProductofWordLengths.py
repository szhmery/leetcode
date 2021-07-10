from typing import List


class Solution:
    #bit manipulation
    def maxProduct(self, words: List[str]) -> int:
        res = 0
        masks = []

        for i in range(len(words)):
            mask = 0
            for c in words[i]:
                mask |= 1 << (ord(c) - ord('a'))
            masks.append(mask)
            for j in range(i):
                if not (masks[i] & masks[j]):
                    res = max(res, len(words[i]) * len(words[j]))
        return res



    # force brute
    def maxProduct2(self, words: List[str]) -> int:
        set_dict = {}
        res = 0
        for word in words:
            cur = set(word)
            for s in set_dict.keys():
                if len(cur.intersection(set(s))) == 0:
                    res = max(res, len(word) * set_dict[s])
            set_dict[word] = len(word)
        return res

solution = Solution()
words = ["abcw","baz","foo","bar","xtfn","abcdef"]
print(solution.maxProduct(words))
print(solution.maxProduct2(words))
words =["a","ab","abc","d","cd","bcd","abcd"]
print(solution.maxProduct(words))
print(solution.maxProduct2(words))
