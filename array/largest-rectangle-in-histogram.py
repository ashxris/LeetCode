class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        stack = []  # Stores indices of the heights array
        max_area = 0
        
        for i in range(n):
            # While stack is not empty and current bar is shorter than the bar at stack top
            while stack and heights[stack[-1]] > heights[i]:
                height = heights[stack.pop()]
                # Determine the width
                # If stack is empty, it means this height extends all the way to the left (index 0)
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
            
        # Process remaining bars in the stack
        while stack:
            height = heights[stack.pop()]
            width = n if not stack else n - stack[-1] - 1
            max_area = max(max_area, height * width)
            
        return max_area