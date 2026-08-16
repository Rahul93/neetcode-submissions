class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        is_present = set(nums)
        res = 0
        
        for num in nums:
            if num-1 not in is_present: 
                streak, curr = 0,num
                while curr in is_present:
                    streak +=1
                    curr += 1
                res = max(res, streak)

        return res