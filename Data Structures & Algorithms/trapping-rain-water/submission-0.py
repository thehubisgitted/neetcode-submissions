class Solution:
    def trap(self, height: List[int]) -> int:
        left_bound = [0] * len(height)
        right_bound = [0] * len(height)
        min_bound = [0] * len(height)

        tallest_left = 0
        for i in range(len(height)):
            h = height[i]
            left_bound[i] = tallest_left
            if h > tallest_left:
                tallest_left = h

        tallest_right = 0
        for i in range(len(height)-1, -1, -1):
            h = height[i]
            right_bound[i] = tallest_right
            if h > tallest_right:
                tallest_right = h
        #print(left_bound)
        #print(right_bound)
        water_sum = 0
        for i in range(len(height)):
            h = height[i]
            water = min(left_bound[i], right_bound[i]) - h
            if water < 0:
                water = 0
            water_sum = water_sum + water
        return water_sum
