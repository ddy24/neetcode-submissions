class Solution:
    def twoSum(self, nums:List[int], target:int)->List[int]:
        dictionary = {} #key: diff, value: index
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff not in dictionary:
                dictionary[nums[i]] = i
            else:
                return [dictionary[diff],i]
                