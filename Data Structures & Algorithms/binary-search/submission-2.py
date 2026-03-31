class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            if target == nums[l]:
                return l
            if target == nums[r]:
                return r
            m = l + ((r-l)//2)
            if target == nums[m]:
                return m
            elif target < nums[m]:
                r = m - 1
            else:
                l = m + 1
        return -1
        