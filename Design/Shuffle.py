import random



class Solution:
    def __init__(self, nums):
        self.array = nums
        self.original = list(nums)

    def reset(self):
        self.array = self.original
        self.original = list(self.original)
        return self.original

    # Complexity Analysis
    # Time complexity : O(n^2)
    # The quadratic time complexity arises from the calls to list.remove (or list.pop), which run in linear time.
    # n linear list removals occur, which results in a fairly easy quadratic analysis.
    # Space complexity : O(n)
    # Because the problem also asks us to implement reset, we must use linear additional space to store the original array.
    # Otherwise, it would be lost upon the first call to shuffle.
    def shuffle(self):
        aux = list(self.array)

        for idx in range(len(self.array)):
            remove_idx = random.randrange(len(aux))
            self.array[idx] = aux.pop(remove_idx)

        return self.array

    # Complexity Analysis
    # Time complexity : O(n)
    # The Fisher-Yates algorithm runs in linear time, as generating a random index and swapping two values can be done
    # in constant time.
    # Space complexity : O(n)
    # Although we managed to avoid using linear space on the auxiliary array from the brute force approach,
    # we still need it for reset, so we're stuck with linear space complexity.
    def shuffle2(self):
        n = len(self.array)
        for idx in range(n):
            swap_index = random.randrange(idx, n)
            self.array[idx], self.array[swap_index] = self.array[swap_index], self.array[idx]
        return self.array


if __name__ == '__main__':
    nums = [1, 2, 3]
    # Your Solution object will be instantiated and called as such:
    obj = Solution(nums)
    param_1 = obj.reset()
    print('original:{0}, reset:{1},'.format(nums, param_1))
    param_2 = obj.shuffle2()
    print('shuffle:{}'.format(param_2))
