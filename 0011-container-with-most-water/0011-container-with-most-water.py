class Solution:
    def maxArea(self, height: list[int]) -> int:
        l=0
        r=len(height)-1
        res=0
        while l<r:
            h=min(height[l],height[r])
            b=r-l
            res=max(res,b*h)
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return res