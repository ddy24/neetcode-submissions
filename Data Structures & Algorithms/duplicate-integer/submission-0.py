class Solution:
    def hasDuplicate(self, nums):
        d=set()
        for n in nums:
            if n in d:
                return True
            d.add(n)
        return False