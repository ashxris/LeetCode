class Solution:
    def findDuplicate(self, nums: list[int]) -> int:

        fast = nums[nums[0]]
        slow = nums[0]
        while fast!=slow:
            slow = nums[slow]
            fast = nums[nums[fast]]
        slow2 = 0
        while slow2!=slow:
            slow = nums[slow]
            slow2 = nums[slow2]
        return slow