'''
Given an integer array nums, return an array answer such that answer[i] is equal to the 
product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
'''

def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = 1
        postfix = 1
        result = [1] * len(nums)

        for i in range(len(nums)):
            result[i] *= prefix
            prefix *= nums[i]
            result[len(nums) - 1 - i] *= postfix
            postfix *= nums[len(nums) - 1 - i]
        
        return result

# https://www.youtube.com/watch?v=bNvIQI2wAjk