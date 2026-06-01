class Solution:
    def findMin(self, nums: List[int]) -> int:

        low=0
        high=len(nums)-1
        last=high
        ans=-1

        while low<=high:
            guess=(low+high)//2
            if nums[guess]>nums[last]:
                 #part-2
                low=guess+1
            else:
                ans=guess
                high=guess-1
        
        return nums[ans]
