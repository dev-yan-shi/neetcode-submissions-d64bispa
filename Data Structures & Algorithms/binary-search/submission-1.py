class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1
        while l<=r:
            if target == nums[l]:
                return l
            if target == nums[r]:
                return r
            if target == nums[l + ((r-l)//2)]:
                return l + ((r-l)//2)
            elif target < nums[l + ((r-l)//2)]:
                r = l + ((r-l)//2) - 1
            else:
                l = l + ((r-l)//2) + 1
        return -1
        