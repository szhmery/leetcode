from typing import List
from collections import Counter

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        element = []
        candidates.sort()
        self.helper(ans, element, Counter(candidates), target)
        return ans

    def helper(self, ans, element, counter, target):
        if target == 0:
            temp = sorted(element)
            if temp in ans:
                return
            else:
                ans.append(element[::])
                return
        for num in counter:
            if counter[num] > 0:
                if target - num >= 0:
                    counter[num] -= 1
                    element.append(num)
                    self.helper(ans, element, counter, target - num)
                    element.pop()
                    counter[num] += 1

    def combinationSum2_2(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(comb, remain, curr, counter, results):
            if remain == 0:
                # make a deep copy of the current combination
                #   rather than keeping the reference.
                results.append(list(comb))
                return
            elif remain < 0:
                return

            for next_curr in range(curr, len(counter)):
                candidate, freq = counter[next_curr]

                if freq <= 0:
                    continue

                # add a new element to the current combination
                comb.append(candidate)
                counter[next_curr] = (candidate, freq - 1)

                # continue the exploration with the updated combination
                backtrack(comb, remain - candidate, next_curr, counter, results)

                # backtrack the changes, so that we can try another candidate
                counter[next_curr] = (candidate, freq)
                comb.pop()

        results = []  # container to hold the final combinations
        counter = Counter(candidates)
        # convert the counter table to a list of (num, count) tuples
        counter = [(c, counter[c]) for c in counter]

        backtrack(comb=[], remain=target, curr=0,
                  counter=counter, results=results)

        return results


    def combinationSum2_3(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(comb, remain, curr, results):

            if remain == 0:
                # make a deep copy of the resulted combination
                results.append(list(comb))
                return

            for next_curr in range(curr, len(candidates)):

                if next_curr > curr \
                        and candidates[next_curr] == candidates[next_curr - 1]:
                    continue

                pick = candidates[next_curr]
                # optimization: skip the rest of elements starting from 'curr' index
                if remain - pick < 0:
                    break

                comb.append(pick)
                backtrack(comb, remain - pick, next_curr + 1, results)
                comb.pop()

        candidates.sort()

        comb, results = [], []
        backtrack(comb, target, 0, results)

        return results


if __name__ == '__main__':
    solution = Solution()
    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    result = solution.combinationSum2(candidates, target)
    print(result)

    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    result = solution.combinationSum2_2(candidates, target)
    print(result)


    candidates = [10, 1, 2, 7, 6, 1, 5]
    target = 8
    result = solution.combinationSum2_3(candidates, target)
    print(result)

    candidates = [2, 5, 2, 1, 2]
    target = 5
    result = solution.combinationSum2_3(candidates, target)
    print(result)

