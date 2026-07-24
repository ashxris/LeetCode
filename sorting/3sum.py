class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()  # Step 1: Sort the array
        res = []
        n = len(nums)
        
        for i in range(n - 2):
            # Skip duplicate values for the first element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Optimization: If the smallest possible sum with nums[i] is > 0, stop early
            if nums[i] + nums[i + 1] + nums[i + 2] > 0:
                break
                
            # Optimization: If nums[i] with the largest elements is < 0, move to next i
            if nums[i] + nums[n - 2] + nums[n - 1] < 0:
                continue
            
            left, right = i + 1, n - 1
            
            # Step 2: Two-pointer search for the remaining two numbers
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    
                    # Skip duplicate values for left pointer
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    
                    # Skip duplicate values for right pointer
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                        
                elif total < 0:
                    left += 1  # Sum is too small, increase left pointer
                else:
                    right -= 1  # Sum is too large, decrease right pointer
                    
        return res