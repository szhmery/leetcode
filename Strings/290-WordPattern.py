class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_array = s.split()
        if len(pattern) != len(s_array):
            return False
        word_set = set()
        map_dict = {}
        for i in range(len(pattern)):
            if pattern[i] in map_dict:
                if s_array[i] != map_dict[pattern[i]]:
                    return False
            else:
                if s_array[i] in word_set:
                    return False
                else:
                    map_dict[pattern[i]] = s_array[i]
                    word_set.add(s_array[i])
        return True
    #https://www.bilibili.com/video/BV1HZ4y1N7wD
    def wordPattern2(self, pattern: str, s: str) -> bool:
        s_array = s.split(" ")
        if len(pattern) != len(s_array):
            return False
        dic1, dic2 = {}, {}
        for p, w in zip(pattern,s_array):
            if p not in dic1:
                dic1[p] = w
            elif dic1[p] != w:
                return False
            if w not in dic2:
                dic2[w] = p
            elif dic2[2] != p:
                return False
        return True


if __name__ == "__main__":
    solution = Solution()

    pattern = "abba"
    s = "dog cat cat dog"
    print(solution.wordPattern(pattern, s))

    pattern = "abba"
    s = "dog cat cat fish"
    print(solution.wordPattern(pattern, s))

    pattern = "aaaa"
    s = "dog cat cat dog"
    print(solution.wordPattern(pattern, s))

    pattern = "abba"
    s = "dog dog dog dog"
    print(solution.wordPattern(pattern, s))
