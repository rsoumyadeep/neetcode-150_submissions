class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasSeen={}
        for i in range(len(nums)):
            if (target - nums[i]) in hasSeen:
                return [hasSeen[target-nums[i]],i]
            hasSeen[nums[i]]=i
        return
        