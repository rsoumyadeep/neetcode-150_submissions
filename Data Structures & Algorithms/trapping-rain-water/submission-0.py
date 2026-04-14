class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        max_left=[0]*n
        max_right=[0]*n

        current_water=0

        for i in range(1,len(height)):
            max_left[i]=max(max_left[i-1],height[i-1])
        for i in range(len(height)-2,-1,-1):
            max_right[i]=max(max_right[i+1],height[i+1])
        
        for i in range(len(height)):
            if(min(max_left[i],max_right[i])-height[i]>=0):
                current_water+=min(max_left[i],max_right[i])-height[i]
        return current_water

        