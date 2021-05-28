from typing import List


class Solution:
    # https://www.bilibili.com/video/BV1Et4y1i7YZ
    def summaryRanges(self, nums: List[int]) -> List[str]:
        l = len(nums)
        if l == 0:
            return []
        nums.append(float('inf'))
        res, start = [], 0
        for i in range(l):
            if nums[i + 1] != nums[i] + 1:
                res.append(str(nums[i]) if i == start else "%s->%s" % (nums[start], nums[i]))
                start = i + 1
        return res


    def summaryRanges2(self, nums: List[int]) -> List[str]:
        ans = []
        if len(nums) == 0:
            return ans
        if len(nums) == 1:
            return [str(nums[0])]
        cur = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                cur.append(nums[i])

            else:
                if len(cur) == 1:
                    ans.append(str(cur[0]))
                else:
                    ans.append(str(cur[0]) + "->" + str(cur[-1]))
                cur = [nums[i]]
        if len(cur) == 1:
            ans.append(str(cur[0]))
        else:
            ans.append(str(cur[0]) + "->" + str(cur[-1]))
        return ans


if __name__ == "__main__":
    solution = Solution()
    nums = [0, 2, 3, 4, 6, 8, 9]
    print("Before:{}".format(nums))
    result = solution.summaryRanges(nums)
    print(result)
    nums = [0, 2, 3, 4, 6, 8, 9]
    result = solution.summaryRanges2(nums)
    print(result)
    nums = [1, 2, 4, 5,7]
    print("Before:{}".format(nums))
    result = solution.summaryRanges(nums)
    print(result)
    nums = [1, 2, 4, 5, 7]
    result = solution.summaryRanges2(nums)
    print(result)