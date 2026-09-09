class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        temp = set()

        for i, n in enumerate(nums):
            if n in temp:
                return True
            temp.add(n)
        
        return False