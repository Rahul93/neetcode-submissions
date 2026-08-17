class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        is_present = {}
        ans = 0
        left = 0

        for right, c in enumerate(s):
            if c in is_present:
                left = max(left, is_present[c] + 1)

            is_present[c] = right
            ans = max(ans, right - left + 1)

        return ans