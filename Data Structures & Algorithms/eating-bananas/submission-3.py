import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def condition(k):
            """
            Returns True if Koko can finish all bananas
            within h hours at speed k.
            """
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / k)

            return hours <= h

        l, r = 1, max(piles)
        result = r

        while l <= r:
            k = (l + r) // 2

            if condition(k):
                result = k
                r = k - 1
            else:
                l = k + 1

        return result