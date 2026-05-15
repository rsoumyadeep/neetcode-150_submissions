class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq=defaultdict(int)

        for n in nums:
            freq[n]+=1
        
        n=len(nums)
        majority=n//2

        for key,value in freq.items():
            if value>majority:
                return key
        