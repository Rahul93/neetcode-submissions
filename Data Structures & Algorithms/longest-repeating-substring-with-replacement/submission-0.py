class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start,end=0,0
        maxCount,maxLength = 0,0
        window = defaultdict(int)

        for end,ch in enumerate(s):
            window[ch] += 1
            maxCount = max(maxCount, window[ch])

            if (end-start+1 - maxCount) > k:
                window[s[start]] -= 1
                start += 1
            
            maxLength = max(maxLength, end-start+1)

        return maxLength



        