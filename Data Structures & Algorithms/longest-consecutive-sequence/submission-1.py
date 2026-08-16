class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        is_present = set()
        res = 0

        for i in nums:
            is_present.add(i)
        
        for num in nums:
            if num-1 not in is_present: 
                streak, curr = 0,num
                while curr in is_present:
                    streak +=1
                    curr += 1
                res = max(res, streak)

        return res