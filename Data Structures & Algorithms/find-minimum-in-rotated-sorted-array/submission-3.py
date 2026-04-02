class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 1,2,3,4,5,6
        # 6,1,2,3,4,5
        # 5,6,1,2,3,4
        # 4,5,6,1,2,3
        # 3,4,5,6,1,2
        # 2,3,4,5,6,1
        # 1,2,3,4,5,6
    
        l,r = 0, len(nums)-1
        
        while l<=r:
            if nums[l]<=nums[r]:
                return nums[l]
            m = l + (r-l)//2
            if (m==r or nums[m]<=nums[r]) and (m==l or nums[m-1]>=nums[l]):
                return nums[m]
            if nums[m] <= nums[r]:
                r = m-1
            else:
                l = m+1
        return nums[m]
        
        
        