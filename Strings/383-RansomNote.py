from collections import Counter


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        l1 = len(ransomNote)
        l2 = len(magazine)
        if l1 > l2:
            return False
        r_list = list(ransomNote)
        m_list = list(magazine)

        for c in r_list:
            if c in m_list:
                m_list.remove(c)
            else:
                return False
        return True

    # https://www.bilibili.com/video/BV1GQ4y1N7Q5
    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        ct_s = Counter(ransomNote)
        ct_m = Counter(magazine)
        for key in ct_s:
            if ct_s[key] > ct_m[key]:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()

    ransomNote = "aa"
    magazine = "aab"
    print(solution.canConstruct(ransomNote, magazine))
    print(solution.canConstruct2(ransomNote, magazine))
    ransomNote = "baa"
    magazine = "aab"
    print(solution.canConstruct(ransomNote, magazine))
    print(solution.canConstruct2(ransomNote, magazine))
    ransomNote = "baac"
    magazine = "aab"
    print(solution.canConstruct(ransomNote, magazine))
    print(solution.canConstruct2(ransomNote, magazine))
