class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        low,high=1,max(piles)
        ans=1

        def canEat(k):
            hours=0
            for pile in piles:
                hours+=math.ceil(pile/k)
            return hours<=h

        while low<=high:
            guess=(low+high)//2
            
            if canEat(guess):
                ans=guess
                high=guess-1
            else:
                low=guess+1
        return ans
