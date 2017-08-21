class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        nums.sort()
        min_sum = 0
        
        for i in range(nums_len):
            if i%2 == 0:
                min_sum +=nums[i]
                
        return min_sum