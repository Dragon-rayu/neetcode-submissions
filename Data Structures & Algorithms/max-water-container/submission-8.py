class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        maximum=0
        while l<r:
            height= min(heights[l],heights[r])
            width=r-l
            area=height*width
            maximum=max(maximum,area)
            if heights[r]>heights[l]:
                l=l+1
            else:
                r=r-1
        return maximum