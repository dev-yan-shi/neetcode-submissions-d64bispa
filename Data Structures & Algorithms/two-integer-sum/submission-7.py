class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ## hashmap in single pass
        ntoi = {}
        for i, num in enumerate(nums):
            
            diff = target - num
            if diff in ntoi:
                return [ntoi[diff], i]
            ntoi[num] = i
        return []
        