class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## hashmap approach
        ntoi = {}
        for i, num in enumerate(nums):
            ntoi[num] = i
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in ntoi and ntoi[diff]!=i:
                return [i, ntoi[diff]]
        return []
        