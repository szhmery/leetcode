from typing import List


class Solution:
    def numRescueBoats2(self, people: List[int], limit: int) -> int:
        if not people or len(people) == 0:
            return 0
        people.sort()
        i, j = 0, len(people) - 1
        ans = 0
        while i <= j:
            ans += 1
            if people[i] + people[j] <= limit:
                i += 1
            j -= 1
        return ans

    # each boat can carry more than 2 people
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        res = 0
        l = 0
        r = len(people) - 1
        while l <= r:
            if people[l] == limit:
                res += 1
                l += 1
            elif people[l] < limit:
                cur = people[l]
                while l <= r and cur < limit:
                    cur = cur + people[r]
                    if cur <= limit:
                        r -= 1
                    else:
                        break
                res += 1
                l += 1

        return res


if __name__ == "__main__":
    solution = Solution()
    people = [1, 2]
    limit = 3
    result = solution.numRescueBoats(people, limit)
    print(result)
    people = [3, 2, 2, 1]
    limit = 3
    result = solution.numRescueBoats2(people, limit)
    print(result)
    people = [3, 5, 3, 4]
    limit = 5
    result = solution.numRescueBoats(people, limit)
    print(result)
    people = [2, 49, 10, 7, 11, 41, 47, 2, 22, 6, 13, 12, 33, 18, 10, 26, 2, 6, 50, 10]
    limit = 50
    result = solution.numRescueBoats(people, limit)
    print(result)
    people = [2, 49, 10, 7, 11, 41, 47, 2, 22, 6, 13, 12, 33, 18, 10, 26, 2, 6, 50, 10]
    limit = 50
    result = solution.numRescueBoats2(people, limit)
    print(result)
