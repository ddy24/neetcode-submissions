class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsCounter = Counter(nums)
        bucket = [[] for i in range(len(nums)+1)]
        #put the number count in the bucket
        for number, count in numsCounter.items():
            bucket[count].append(number)
        res = []
        for freq in reversed(bucket):
            for num in freq:
                res.append(num)
                if len(res)== k:
                    return res