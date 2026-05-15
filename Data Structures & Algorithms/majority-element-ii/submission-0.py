class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        freq=defaultdict(int)

        for n in nums :
            freq[n]+=1
        
        thresold=len(nums)//3

        result=[]
        
        for num,count in freq.items():
            if count > thresold:
                result.append(num)
        return result