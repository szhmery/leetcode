# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import itertools
def solution(A, B, C, D):
    # write your code in Python 3.6
    ans = 0
    nums = [A, B, C, D]

    hm_set = set()
    # enumerate all possibilities, with the permutation() func
    for h, i, j, k in itertools.permutations(nums):
        hour = h * 10 + i
        minute = j * 10 + k
        if hour < 24 and minute < 60 and str(hour)+str(minute) not in hm_set:
            # print(str(hour) + ":" + str(minute))
            hm_set.add(str(hour)+str(minute))
            ans += 1

    return ans
    # for i in range(4):
    #     for j in range(4):
    #         if j != i:
    #             for k in range(4):
    #                 if k != i and k != j:
    #                     l = 6 - i - j - k
    #                     hour = 10 * nums[i] + nums[j]
    #                     min = 18 * nums[k] + nums[l]
    #                     if hour < 24 and min < 60 and  (hour * 100 + min) not in exist:
    #                         print(str(hour)+":"+str(min))
    #                         ans += 1
    #                         exist.add(hour * 100 + min)
    #
    # return ans


def largestTimeFromDigits( A, B, C, D) -> str:
    nums = [A, B, C, D]
    ans = 0
    hm_set = set()
    def create(permutation):
        nonlocal ans
        h, i, j, k = permutation
        hour = h * 10 + i
        minute = j * 10 + k
        if hour < 24 and minute < 60 and str(hour)+str(minute) not in hm_set:
            ans += 1
            hm_set.add(str(hour) + str(minute))

    def permutate(nums, start):
        if start == len(nums):
            create(nums)
            return

        for index in range(start, len(nums)):
            nums[index], nums[start] = nums[start], nums[index]
            permutate(nums, start + 1)
            nums[index], nums[start] = nums[start], nums[index]

    permutate(nums, 0)
    return ans

result = solution(1,8,3,2)
print(result)

result = solution(2, 3, 3, 2)
print(result)
print(largestTimeFromDigits(1,8,3,2))
print(largestTimeFromDigits(2, 3, 3, 2))