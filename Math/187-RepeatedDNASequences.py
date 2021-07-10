from typing import List
class Solution:
    # bit manipulation
    #https://www.bilibili.com/video/BV1Na4y1L7eZ?from=search&seid=4482732933281136300
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seq = set()
        ans = set()
        map_seq = {'A':0, 'C':1, 'G': 2, 'T': 3}
        if len(s) < 10:
            return []
        hash_key = 0
        for i in range(9):
            hash_key = (hash_key << 2) | map_seq[s[i]]
        for i in range(9, len(s)):
            # 0x3ffff means just moves the 18 lowest bits and then adds 2 bits, constructs 20 bits.
            hash_key = ((hash_key & 0x3ffff) << 2) | map_seq[s[i]]
            if hash_key in seq:
                ans.add(s[i - 9: i + 1])
            else:
                seq.add(hash_key)
        return ans

    def findRepeatedDnaSequences2(self, s: str) -> List[str]:
        seq = set()
        ans = set()
        for i in range(len(s) - 9):
            cur = s[i : i + 10]
            if cur in seq:
                ans.add(cur)
            else:
                seq.add(cur)
        return list(ans)
solution = Solution()
print(solution.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
print(solution.findRepeatedDnaSequences("AAAAAAAAAAAAA"))
