class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        out = []
        for i in range(len(nums)-1):
            j = i+1
            while j<len(nums):
                if(nums[i]+ nums[j] == target):
                    out.append(i)
                    out.append(j)
                    return out
                    break
                j+=1
        return out
        
        