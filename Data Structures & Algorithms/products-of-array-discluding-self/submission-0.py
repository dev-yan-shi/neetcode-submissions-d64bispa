class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_zeros = 0
        prod = 1
        for n in nums:
            if n !=0:
                prod*=n
            else:
                num_zeros+=1
        res = []
        if num_zeros > 1:
            return [0]*len(nums)
        for n in nums:
            if n==0:
                res.append(prod)
            elif n!=0 and num_zeros==1:
                res.append(0)
            else:
                res.append(int(prod/n))
        return res



        