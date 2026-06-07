class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countNums = Counter(nums)
        bucket = [ [] for _ in range(len(nums)+1)] #freq of number
        print(bucket)
        for num, freq in countNums.items():
            bucket[freq].append(num) #这里一定是append,而不是等于，因为可能有很多个
        res = []
        for i in range(len(nums),0,-1):
            for num in bucket[i]:
                res.append(num)
            if len(res)== k:
                return res