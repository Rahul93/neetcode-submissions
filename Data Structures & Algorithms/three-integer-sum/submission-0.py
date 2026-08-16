class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        hashmap = {}

        res = set()

        for i in range(n):
            for j in range(i,n):
                val = -(nums[i]+nums[j])
                if i != j and val in hashmap and hashmap[val] != i and hashmap[val] != j:
                    triplet = sorted([nums[i],nums[j],val])
                    res.add(tuple(triplet))
                if nums[j] not in hashmap:
                    hashmap[nums[j]] = j
        return list(res)