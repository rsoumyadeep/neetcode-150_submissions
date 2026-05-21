class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l,r=1,max(piles)
        result=r
        while l<=r :
            rate=(l+r)//2
            hours=0
            for p in piles :
                hours+=math.ceil(p/rate)
            
            if hours<=h:
                result=min(result,rate)
                r=rate-1
            else :
                l=rate+1
        
        return result