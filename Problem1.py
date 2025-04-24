# Problem 1 : Repeated DNA Sequences
# Time Complexity : 
'''
Hash Set - O(n) where n is the length of the string
Sliding Window - O(n) where n is the length of the string
'''
# Space Complexity : 
'''
Hash Set - O(n) where n is the length of the string
Sliding Window - O(n) where n is the length of the string
'''
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this :
'''
None
'''

# Your code here along with comments explaining your approach
# Hash Set
def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # get the length of the string s
        length = len(s)
        # define hash set for all the subsequence and for result 
        allSubs = set()
        result = set()
        # loop from 0 to (length-9)
        for i in range(length-9):
            # get the subsequence of string (10 character from ith character)
            currSub = s[i:i+10]
            # check if the sub sequence is already present in the allSubs hash set
            if currSub in allSubs:
                # if it is then add the subsequence in the result set
                result.add(currSub)
            else:
                # else add the subsequence to the allSubs hash set
                allSubs.add(currSub)
        # convert the result hash set to list then return that list
        return list(result)

# Sliding Window
from typing import List
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        # get the length of the string s
        length = len(s)
        # if the length of the string is less than 10 then return empty []
        if length < 10:
            return []
        # define map dictionary where character is key and number as value
        map = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
        # define hash set for all the subsequence and for result 
        allSubs = set()
        result = set()
        # define variable currHash which store current hash and set to 0 
        currHash = 0

        # loop from 0 to 10 for first characters
        for i in range(10):
            # calculate the hash for the subsequence as (current hash * 4  +  value of the map for the key(character at ith position of source string))
            currHash = currHash * 4 + map[s[i]]
        # add the value o currHash to allSubs set
        allSubs.add(currHash)

        # define the power variable and set to 4 raise to 9
        power = 4 ** 9

        # loop from 1 to (length-9)
        for i in range(1, length-9):
            # out character
            # get the character which will be out of the sliding window
            outChar = s[i-1]
            # remove the hash value of the out character from the currentHash of the sequence
            currHash = currHash - power * map[outChar]

            # in character
            # get the character which will be included in the sliding window
            inChar = s[i+9]
            # add the hash value of the in character to the currHash of the sequence
            currHash = currHash * 4 + map[inChar]

            # check if currHash of the sequence is part of the allSubs set
            if currHash in allSubs:
                # if it is then add subsequence to the result set
                result.add(s[i:i+10])
            else:
                # else add the currHash of the subsequence to the allSubs set
                allSubs.add(currHash)

        # convert the result hash set to list then return that list
        return list(result)
