class Solution:
    def replaceSpace(self, s: str) -> str:
        arr = []
        for c in s:
            if c != ' ':
                arr.append(c)
            else:
                arr.append('%20')
        return ''.join(arr)

    def replaceSpace2(self, s: str) -> str:
        return s.replace(' ','%20')

so = Solution()
print(so.replaceSpace('We are family.'))