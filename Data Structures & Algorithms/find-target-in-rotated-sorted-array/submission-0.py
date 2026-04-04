class Solution:
    def binary_search(self, nums: List[int], target:int, start_i:int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums)-1
        while l<=r:
            m = (l+r)//2
            if nums[m] == target:
                return (start_i+m)
            if nums[m] < target:
                l = m+1
            else:
                r = m-1
        return -1
        

    def search(self, nums: List[int], target: int) -> int:
        # 1,2,3,4,5,6
        # 6,1,2,3,4,5
        # 5,6,1,2,3,4
        # 4,5,6,1,2,3
        # 3,4,5,6,1,2
        # 2,3,4,5,6,1
        # 1,2,3,4,5,6

        l,r = 0, len(nums)-1
        min_val = float('inf')
        min_idx = -1
        while l<=r:
            if nums[l] <= nums[r]:
                min_idx = l if nums[l]<min_val else min_idx
                min_val = nums[min_idx]
                # print("new min idx, ", min_idx)
                # print("breaking loop")
                break
                #return self.binary_search(nums[l:r], target, l)
            m = (l+r)//2
            #print("curr m:", m)
            min_idx = m if nums[m]<=min_val else min_idx
            min_val = nums[min_idx]
            #print("new min idx, ", min_idx)
            if nums[m] <=nums[r]:
                r = m-1
            else:
                l = m+1
        #print("minimum idx is:", min_idx)
        if nums[min_idx] > target:
            return -1
        elif nums[min_idx] == target:
            return min_idx
        else:
            s1 = self.binary_search(nums[min_idx:], target, min_idx)
            s2 = self.binary_search(nums[:min_idx], target, 0)
            if s1==-1 and s2==-1:
                return -1
            else:
                return s1 if s1!=-1 else s2


