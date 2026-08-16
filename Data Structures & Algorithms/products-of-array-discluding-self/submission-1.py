class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) == 2:
            nums.reverse()
            return nums

        lArray = []
        rArray=[]
        ans=[]
        pr = 1
        for n in nums:
            pr = pr*n
            lArray.append(pr)
        pr = 1
        print(lArray)
        for n in reversed(nums):
            pr = pr*n
            rArray.append(pr)
        rArray.reverse()
        print(rArray)
        ans.append(rArray[1])
        for i in range(1, len(nums)-1):
            ans.append(lArray[i-1]*rArray[i+1])

        ans.append(lArray[len(nums)-2])
        return ans