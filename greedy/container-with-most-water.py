class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = maxwater = 0
        right = len(height) - 1

        while left < right:

            currarea = (right -left) * min(height[left], height[right])
            maxwater = max(currarea, maxwater)

            if height[left]< height[right]:
                left+=1
            else:
                right-=1
        return maxwater

        