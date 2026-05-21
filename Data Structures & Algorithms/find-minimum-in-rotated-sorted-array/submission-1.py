class Solution:
    def findMin(self, nums: List[int]) -> int:
        result=nums[0]
        l,r=0,len(nums)-1

        while l<=r:
            if nums[l] < nums[r]:
                result=min(result,nums[l])
                break

            mid= (l+r)//2
            result=min(result,nums[mid])

            if nums[l]<=nums[mid]:
                l=mid+1
            else:
                r=mid-1
        
        return result

        