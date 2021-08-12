from typing import List
import functools
#https://leetcode-cn.com/problems/ba-shu-zu-pai-cheng-zui-xiao-de-shu-lcof/solution/mian-shi-ti-45-ba-shu-zu-pai-cheng-zui-xiao-de-s-4/
def minNumber(nums:List)->str:
    def sort_rule(x, y):
        a, b = x + y, y + x
        if a > b:
            return 1
        elif a < b:
            return -1
        else:
            return 0
    strs = [str(num) for num in nums]
    strs.sort(key = functools.cmp_to_key(sort_rule))
    return ''.join(strs)

def minNumber2(nums:List)->str:
    def quick_sort(low, high):
        if low >= high:
            return
        i, j = low, high
        while i < j:
            while i < j and strs[j] + strs[low] >= strs[low] + strs[j]:
                j -= 1
            while i < j and strs[i] + strs[low] <= strs[low] + strs[i]:
                i += 1
            strs[i], strs[j] = strs[j], strs[i]
        strs[i], strs[low] = strs[low], strs[i]
        quick_sort(low, i - 1)
        quick_sort(i + 1, high)

    strs = [str(num) for num in nums]
    quick_sort(0, len(strs) - 1)
    return ''.join(strs)

print(minNumber([3, 32, 321]))
print(minNumber([4,3,2,1]))
print(minNumber2([3, 32, 321]))
print(minNumber2([4,3,2,1]))