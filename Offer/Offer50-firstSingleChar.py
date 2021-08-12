class Solution:
    # 时间复杂度 O(N)O(N) ： NN 为字符串 s 的长度；需遍历 s 1轮，使用 O(N) ；HashMap 查找操作的复杂度为 O(1) ；
    # 空间复杂度 O(1) ： 由于题目指出 s 只包含小写字母，因此最多有 26 个不同字符，HashMap 存储需占用 O(26)=O(1) 的额外空间。

    def firstUniqChar(self, s: str) -> str:

        #Python 3.6 后，默认字典就是有序的，因此无需使用 OrderedDict()
        dic = {}
        for c in s:
            dic[c] = not c in dic
        for k, v in dic.items():
            if v: return k
        return ' '

    #时间复杂度 O(N)O(N) ： NN 为字符串 s 的长度；需遍历 s 两轮，使用 O(N) ；HashMap 查找操作的复杂度为 O(1) ；
    #空间复杂度 O(1) ： 由于题目指出 s 只包含小写字母，因此最多有 26 个不同字符，HashMap 存储需占用 O(26)=O(1) 的额外空间。

    def firstUniqChar2(self, s: str) -> str:
        dic = {}
        for c in s:
            dic[c] = not c in dic
        for c in s:
            if dic[c]: return c
        return ' '

