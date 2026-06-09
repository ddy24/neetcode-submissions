class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsCount = Counter(nums)
        numsHeap = []
        for number, count in numsCount.items():
            heapq.heappush(numsHeap,(-count,number))
        res = []
        for _ in range(k):
            item = heapq.heappop(numsHeap)[1]
            res.append(item)
        return res


