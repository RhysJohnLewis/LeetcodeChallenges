
'''
1. Two Sum

Given an array of integers (nums) and an integer (target), 
return indices of the two numbers such that they add up to (target).

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.
'''

# Use this as the sample input twoSum([2,3,11,15], 9)

#Solution
class Solution():
    
    def __init__(self, nums, target):
        self.nums = nums
        self.target = target
    
    def twoSum(self):
        #create blank list
        mylist = []
        # get all numbers in the list
        for a in range(len(self.nums)):
            #for every number in the list, cycle through all numbers starting from 1 after that number
            for b in range(a+1, len(self.nums)):
                #add the two corresponding numbers together and see if they equal target
                if (self.nums[a] + self.nums[b]) == self.target:
                    #append to blank list
                    mylist.append([self.nums[a], self.nums[b]])
        #return mylist
        mylist = mylist[0]
        return mylist   

# =================================================================

#Solution for leetcode - Without encapsulation

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #create blank list
        mylist = []
        # get all numbers in the list
        for a in range(len(nums)):
            #for every number in the list, cycle through all numbers starting from 1 after that number
            for b in range(a+1, len(nums)):
                #add the two corresponding numbers together and see if they equal target
                if (nums[a] + nums[b]) == target:
                    #append to blank list
                    mylist.append([nums[a], nums[b]])
        #I would return mylist, but the question says there is only 1 answer
        oneanswer = mylist[0]
        return oneanswer  
    
    # almost have it, just need to now return the indices of the values, not the values themselves