class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        maxWater = 0

        while left < right:
            width = right - left
            maxWater = max(maxWater, width * (min(heights[left], heights[right])))
            if heights[left] < heights[right]:
                left += 1
            elif heights[left] > heights[right]:
                right -= 1
            elif heights[left] == heights[right]:
                left += 1
        
        return maxWater