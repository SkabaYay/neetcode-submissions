class Solution:
    def maxArea(self, heights: List[int]) -> int:
        start = 0
        end = len(heights) - 1
        maxArea = 0
        width = 0
        height = 0
        area = 0

        while start < end:
            width = end - start
            height = min(heights[start], heights[end])
            area = width * height
            maxArea = max(maxArea, area)
            if heights[start] > heights[end]:
                end -= 1
            else:
                start += 1

        return maxArea