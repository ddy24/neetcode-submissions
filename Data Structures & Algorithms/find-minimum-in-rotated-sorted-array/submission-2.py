class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)# [)
        while l < r:
            mid= (l + r)//2
            if nums[mid] >= nums[0]:
                l = mid + 1
            else:
                r = mid
        if len(nums)== l :
            return nums[0]
        return nums[l]