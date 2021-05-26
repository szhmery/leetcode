class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        word_map = {}
        val_set = set()
        for i in range(len(s)):
            if s[i] in word_map:
                if t[i] != word_map[s[i]]:
                    return False
            else:
                word_map[s[i]] = t[i]
                if t[i] in val_set:
                    return False
                val_set.add(t[i])
        return True
    # https://blog.csdn.net/coder_orz/article/details/51681396
    def isIsomorphic2(self, s: str, t: str) -> bool:
        pos1, pos2 = [-1]*256, [-1]*256
        for i in range(len(s)):
            if pos1[ord(s[i])] != pos2[ord(t[i])]:
                return False
            pos1[ord(s[i])] = pos2[ord(t[i])] = i
        return True
    def isIsomorphic3(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return map(s.find, s) == map(t.find, t)

    def isIsomorphic4(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))



if __name__ == "__main__":
    solution = Solution()
    s = "egg"
    t = 'app'
    print(solution.isIsomorphic(s, t))
    print(solution.isIsomorphic2(s, t))
    s = "badc"
    t = "baba"
    print(solution.isIsomorphic(s, t))
    print(solution.isIsomorphic2(s, t))
    s = "paper"
    t = "title"
    print(solution.isIsomorphic(s, t))
    print(solution.isIsomorphic2(s, t))
    s = "abbc"
    t = "ebba"
    print(solution.isIsomorphic(s, t))
    print(solution.isIsomorphic2(s, t))