class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsCounter = Counter(nums)
        numsHeap = []
        for num, count in numsCounter.items():
            heapq.heappush(numsHeap,(-count,num))
        res = []
        for i in range(k):
            item = heapq.heappop(numsHeap)[1]
            res.append(item)
        return res