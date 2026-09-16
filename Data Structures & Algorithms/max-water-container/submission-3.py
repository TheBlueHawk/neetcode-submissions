class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        max_area = 0
        while l < r:
            max_area = max(max_area, self.area(l,r, heights))
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        return max_area
                

        
    def area(self, l, r, heights):        
        return (r-l)*min(heights[l], heights[r])

    