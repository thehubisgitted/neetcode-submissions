class Solution:
    def maxArea(self, heights: List[int]) -> int:
     start = 0 
     end = len(heights)-1
    
     maxwidth = 0
     while start < end:
        width = end - start
        height = min(heights[start],heights[end])
        area = width * height
        if area > maxwidth:
            maxwidth = area
        if heights[start] < heights[end]:
            start+=1
        else:
            end-=1
    
     return maxwidth