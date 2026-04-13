class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hasSeen = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hasSeen:
                return [hasSeen[complement], i]
            hasSeen[nums[i]] = i
        