class Solution:
    def search(self, nums: List[int], target: int) -> int:

        low=0
        last=len(nums)-1
        high=last
        
        while low<=high:
            guess=(low+high)//2
            if nums[guess]==target:
                return guess
            if nums[guess] > nums[last]: 
                #left sorted array
                if nums[guess]<target or nums[0] > target:
                    low=guess+1
                else:
                    high=guess-1
            else : 
                #right sorted array 
                if nums[guess]>target or nums[last] < target:
                    high=guess-1
                else:
                    low=guess+1
        
        return -1
                