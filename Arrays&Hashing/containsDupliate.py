'''
Given an integer array nums, return true if any value appears at least twice in the 
array, and return false if every element is distinct.
'''

def containsDuplicate(self, nums: List[int]) -> bool:
        # hashset for fast access to visited values
        hashset = set()

        # iterate through the list, if any current value has already been visited, return false
        for i in range(len(nums)):
            if nums[i] in hashset:
                return True
            hashset.add(nums[i])
        return False