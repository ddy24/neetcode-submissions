from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counterNums = Counter(nums)
        sortedCounterNums = sorted(counterNums.items(), key = lambda x:-x[1])
        res = []
        for i in range(k):
            res.append(sortedCounterNums[i][0])
        return res