class Solution:
    def twoSum(self, num: List[int], target: int) -> List[int]:
        l,r = 0, len(num)-1

        while(l<r):
            if num[l] + num[r] == target:
                return [l+1, r+1]
            elif num[l] + num[r] < target:
                l = l+1
            else:
                r = r-1
        
