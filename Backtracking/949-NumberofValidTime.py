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
    # write your code in Python 3.6
    # It uses backtracking algorithm.
    nums = [A, B, C, D]
    # record the total count
    count = 0
    # the set used to save existed valid time.
    hm_set = set()

    def create(permutation):
        nonlocal count
        h, i, j, k = permutation
        hour = h * 10 + i
        minute = j * 10 + k
        # if the time format is invalid or it's existed in the set, will return.
        if hour < 24 and minute < 60 and str(hour) + str(minute) not in hm_set:
            count += 1
            # save the existed hour+minute string to a set.
            hm_set.add(str(hour) + str(minute))

    def permutate(nums, start):
        # if index is 4, we collect 4 digits to calculate time, it reaches the end of the combination.
        if start == len(nums):
            # check whether the time is valid or not.
            create(nums)
            return
        # switch the element between the first position in the array and each of the positions in the array
        for index in range(start, len(nums)):
            nums[index], nums[start] = nums[start], nums[index]
            permutate(nums, start + 1)
            # remember to swap back.
            nums[index], nums[start] = nums[start], nums[index]

    permutate(nums, 0)
    return count


def largestTimeFromDigits2( A, B, C, D) -> str:
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