class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return right - left + 1
            while left < right and s[left] == s[left + 1]:
                left += 1
            while left < right and s[right] == s[right - 1]:
                right -= 1
            left += 1
            right -= 1
        return 1 if left == right else 0
