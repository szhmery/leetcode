from collections import defaultdict
from typing import List


class Solution:
    # https://leetcode.com/problems/single-number/solution/
    def singleNumber_answer4(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a

    def singleNumber(self, nums: List[int]) -> int:
        for num in nums:
            if nums.count(num) == 1:
                return num

    def singleNumber_answer(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        return no_duplicate_list.pop()

    def singleNumber_answer2(self, nums: List[int]) -> int:
        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1

        for i in hash_table:
            if hash_table[i] == 1:
                return i

    def singleNumber_answer3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return 2 * sum(set(nums)) - sum(nums)



if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 3, 2]
    single_num = solution.singleNumber(nums)
    print("single number: {}".format(single_num))

    single_num = solution.singleNumber_answer(nums)
    print("single number: {}".format(single_num))

    single_num = solution.singleNumber_answer2(nums)
    print("single number: {}".format(single_num))

    single_num = solution.singleNumber_answer3(nums)
    print("single number: {}".format(single_num))

    single_num = solution.singleNumber_answer4(nums)
    print("single number: {}".format(single_num))
