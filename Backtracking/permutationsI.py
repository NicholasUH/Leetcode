from collections import List
def permute(self, nums: List[int]) -> List[List[int]]:
    # nums = [1,2,3]
    result = []

    if len(nums) == 1:
    # [1] or [2] or [3]
        return [nums.copy()]

    for i in range(len(nums)):
        n = nums.pop(0)
        perms = self.permute(nums)
    # perms = [[2,3] [3,2]]

    for perm in perms:
        perm.append(n)
    # perms = [[2,3,1] [3,2,1]]
    result.extend(perms)
    nums.append(n)
    return result
    