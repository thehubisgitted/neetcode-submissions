class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        start_index = 0
        end_index = len(heights)-1
        while start_index < end_index:
            width = end_index - start_index
            height = min(heights[start_index], heights[end_index])
            area = width * height

            if area > max_area:
                max_area = area
            if heights[start_index] < heights[end_index]:
                start_index +=1
            else:
                end_index-=1
        return max_area