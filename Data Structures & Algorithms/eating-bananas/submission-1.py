class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # [1,2,3,4] => 1//n + 2//n +... <=9
        ## fastest speed will come when value = max i.e. 4
        ## slowest speed = 1
        ## k=4, 4 hrs
        ## k=3, 5 hrs
        ## k=2, 6 hrs
        ## k=1, 10 hrs
        #piles.sort()
        #print("sorted piles:", piles)
        l,r = 1, max(piles)
        k = 1
        while l<=r:
            t = sum(x//l for x in piles) + sum(x%l!=0 for x in piles)
            print("current t:", t)
            if t<=h:
                return l
            m = l + ((r-l)//2)
            tm = sum(x//m for x in piles) + sum(x%m!=0 for x in piles)
            print("current tm:", tm)
            if tm<=h:
                k = m
                r = m-1
            else:
                l = m+1
        return k
