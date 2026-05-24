class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hasSeen=set()

        for num in nums:
            if num in hasSeen:
                return num
            hasSeen.add(num)
        
    

        