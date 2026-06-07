class Solution:
    def hasDuplicate(self, nums:[list[int]])->bool:
        numSet = set(nums)
        if len(numSet) == len(nums):
            return False
        else:
            return True
        