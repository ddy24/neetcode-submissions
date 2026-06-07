class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sumMap = {} #key:number, value: index
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in sumMap:
                return [sumMap[diff], i]
            else:
                sumMap[nums[i]] = i 
