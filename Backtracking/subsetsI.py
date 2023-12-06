from collections import List

def subsets(self, nums: List[int]) -> List[List[int]]:
    result = []

    subset = []
    def backtrack(index):
        # ends backtracking when all states are made
        if index >= len(nums):
            result.append(subset.copy())
            return
                
        # decision to include
        subset.append(nums[index])
        backtrack(index + 1)
            
        # decision to exclude
        subset.remove(nums[index])
        backtrack(index + 1)


    backtrack(0)
    return result