class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l,r=1,max(piles)
        result=r
        while l<=r:
            k=(l+r)//2
            hours=0
            for p in piles:
                hours+=(p+k-1)//k
            if hours<=h:
                result=min(result,k)
                r=k-1
            else:
                l=k+1
        return result