class Solution:
    def search(self, lists, target):
        start, end = 0, len(lists) - 1

        while start <= end:
            mid = start + (end - start) // 2
            if target == lists[mid]:
                return mid
            # [start,mid] is sorted
            if lists[mid] >= lists[start]:
                if target >= lists[start] and target <= lists[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                # [mid,end] is sorted
                if target >= lists[mid] and target <= lists[end]:
                    start = mid + 1
                else:
                    end = mid - 1
        return -1


if __name__ == "__main__":
    solution = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    result = solution.search(nums, target)
    print(result)
