class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area=0
        stack=[]

        for index,height in enumerate(heights):
            start=index
            while stack and stack[-1][1]>height:
                i,h=stack.pop()
                width=index-i
                max_area=max(max_area,width*h)
                start=i
            stack.append([start,height])
        
        for index,height in stack :
            max_area=max(max_area,(len(heights)-index)*height)
        
        return max_area

        