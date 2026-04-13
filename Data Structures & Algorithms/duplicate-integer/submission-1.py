class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hasSeen=set()
        for n in nums :
            if n in hasSeen:
                return True
            hasSeen.add(n)
        return False
                

            
        