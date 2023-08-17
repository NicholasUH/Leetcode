'''
Given an array of strings strs, group the anagrams together. 
You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or 
phrase, typically using all the original letters exactly once.
'''

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # creates a map to store sorted_word:list of anagrams
        result = defaultdict(list)

        # iterate through array, sort each word and append that to the corresponding sorted_word
        for word in strs:
            sorted_word = "".join(sorted(word))
            result[sorted_word].append(word)

        # return values
        return list(result.values())
