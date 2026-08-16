import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        freq = Counter(nums)
        heap = []
        for num,count in freq.items():
            heapq.heappush(heap,(count,num))

            if len(heap) > k:
                heapq.heappop(heap)

        while(heap):
            freq, num = heapq.heappop(heap)
            ans.append(num)
    
        return ans
        