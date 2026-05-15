class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq=defaultdict(int)

        for n in nums:
            freq[n]+=1
        
        majority=len(nums)//2

        for num,count in freq.items():
            if count>majority:
                return num
        