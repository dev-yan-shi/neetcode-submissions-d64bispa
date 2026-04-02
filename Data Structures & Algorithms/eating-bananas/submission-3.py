class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l,r = 1, max(piles)
        k = 1
        while l<=r:
            # if sum(math.ceil(x/l) for x in piles) <=h:
            #     return l
            m = l + ((r-l)//2)
            if sum(math.ceil(x/m) for x in piles) <=h :
                k = m
                r = m-1
            else:
                l = m+1
        return k
