'''
Given an integer array nums and an integer k, return the k most frequent elements. 
You may return the answer in any order.
'''


def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # store number:frequency in array
        hashmap = defaultdict(int)

        # iterate through array and add the number and its frequency to the hashmap
        for num in nums:
            hashmap[num] += 1


        # store contents of dictionary into a list
        sorted_keys = sorted(hashmap.keys(), key=lambda x: hashmap[x], reverse=True)

        # sorts the keys(values), based on keypair(frequency) given by lambda function, in descending order


        return sorted_keys[:k]