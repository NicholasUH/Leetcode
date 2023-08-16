'''
Given an integer array nums, return true if any value appears at least twice in the 
array, and return false if every element is distinct.
'''


'''Solution 1'''
def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

'''
Explanation:
The idea behind this solution is to check every possible pairing of numbers from the list
using loops

Ex. [1,2,3,1]

Compare 1 to 2,3,1 - Duplicate found
Compare 2 to 3,1
Compare 3 to 1

Problem: The solution is too inefficient as its worst time complexity is O(n^2)
'''



'''Solution 2'''
def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for i in range(len(nums)):
            if nums[i] in hashset:
                return True
            hashset.add(nums[i])
        return False

'''
Explanation:
The idea behind this solution is to be able to store visited values in a data structure
that allows fast access. The best is a hashset as its time complexity for all operations is
O(1). This allows us to only need to iterate through the list once meaning that the time
complexity is O(n)

Ex. [1,2,3,1]

Compare 1 to set{}
Compare 2 to set{1}
Compare 3 to set{1,2}
Compare 1 to set{1,2,3} - Duplicate found
'''