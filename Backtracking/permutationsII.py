from collections import List
def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    result = []
    perm = []
        
    # counter table
    count = {n:0 for n in nums}
    for n in nums:
        count[n] += 1
    
    def backtrack():
        # permutation found
        if len(perm) == len(nums):
            result.append(perm.copy())
        
        # for each unique element, add it to perm, backtrack, then remove it
        for n in count:
            if count[n] > 0:
                perm.append(n)
                count[n] -= 1

                backtrack()

                count[n] += 1
                perm.pop()
    backtrack()
    return result

