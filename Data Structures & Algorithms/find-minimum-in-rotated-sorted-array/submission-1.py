class Solution:
    def bSearch(self, nums, start, end):
        mid = start + (end-start)//2
        
        if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
            return nums[mid + 1]

        
        if mid > 0 and nums[mid] < nums[mid - 1]:
            return nums[mid]
        
        if nums[mid] >= nums[0]:
            return self.bSearch(nums, mid+1,end)
        else:
            return self.bSearch(nums, start, mid-1)

    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if nums[0] < nums[-1] or n == 1:
            return nums[0]
        else:
            return self.bSearch(nums, 0, n-1)


        