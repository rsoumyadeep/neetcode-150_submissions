class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hashMap={} # val : index

        for i,n in enumerate(nums):
            diff=target-n
            if diff in hashMap:
                return [hashMap[diff],i]
            hashMap[n]=i

        return
        