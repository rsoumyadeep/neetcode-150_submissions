class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def canCarry(capacity):
            d=1
            c=0
            for w in weights:
                if c+w>capacity:
                    d+=1
                    c=w
                else:
                    c+=w
            return d<=days

        l=max(weights)
        r=sum(weights)
        ans=l

        while l<=r:
            k=(l+r)//2

            if canCarry(k):
                ans=k
                r=k-1
            else :
                l=k+1
        return ans
        