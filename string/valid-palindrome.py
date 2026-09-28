class Solution:
    def isPalindrome(self, s: str) -> bool:

        news = ''.join(ch for ch in s if ch.isalnum()).lower()

        left = 0
        right = len(news) - 1

        while left < right:
            if news[left] != news[right]:
                return False

            left = left + 1
            right = right - 1
        
        return True
        