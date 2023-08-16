'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or 
phrase, typically using all the original letters exactly once.
'''

def isAnagram(self, s: str, t: str) -> bool:
        # check length as anagrams should have the same amount of letters
        if len(s) != len(t):
            return False

        # hashmap to map a character to its frequency in a string
        sMap, tMap = defaultdict(int),  defaultdict(int)
        
        # iterate through strings and add to hashmap
        for i in range(len(s)):
            sMap[s[i]] += 1
            tMap[t[i]] += 1
        
        # check if the maps are equal, if equal, then the strings are anagrams
        return sMap == tMap
