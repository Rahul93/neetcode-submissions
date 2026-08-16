class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        present = {}

        for i,n in enumerate(nums):
            if target-n in present:
                return [i, present[target-n]] if i < present[target-n] else [present[target-n], i]
            else:
                present[n] = i

        return [-1]
        