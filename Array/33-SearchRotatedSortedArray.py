class Solution:
    # binary search
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

    def search_min_number(self, lists):
        def inorder(l, r):
            res = lists[l]
            for i in range(l + 1, r + 1):
                res = min(res, lists[i])
            return res

        if not lists or len(lists) == 0:
            return
        l = 0
        r = len(lists) - 1
        mid = l
        while nums[l] >= nums[r]:
            if r - l == 1:
                mid = r
                break
            mid = l + (r - l) // 2
            if lists[mid] == lists[l] == lists[r]:
                return inorder(l, r)
            if lists[mid] >= nums[l]:
                l = mid
            else:
                r = mid
        return lists[mid]

if __name__ == "__main__":
    solution = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    result = solution.search(nums, target)
    print(result)
    result = solution.search_min_number(nums)
    print(result)
    nums = [1, 0, 1, 1, 1, 1]
    result = solution.search_min_number(nums)
    print(result)