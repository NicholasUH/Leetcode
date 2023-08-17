'''
Given an array of integers nums and an integer target, return indices of the two numbers 
such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the 
same element twice.

You can return the answer in any order.
'''


def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap to store visited values:indexes
        hashmap = {}

        # iterate through array looking to see if the current value has its complement(targert - current value)
        # inside the hashmap, return indices if it exists, else add value:index to hashmap
        for i in range(len(nums)):
            if target - nums[i] in hashmap:
                return [i,hashmap[target - nums[i]]]
            hashmap[nums[i]] = i  