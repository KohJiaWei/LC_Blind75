'''https://leetcode.com/problems/two-sum/submissions/
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                else:
                    if target == nums[i] + nums[j]:
                        return [i,j]
                      
 #time complexity O(n^2)
 '''
 learnt:
# -> means 'function annotation'
# : also means 'function annotation'

 Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity? 
 
 Thought process : 
 dictionary --> key as index, val as number
 loop and find/return { target - num }
 
'''
  class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     
        hash_table = {}
    #k is key : index     v is value: number
        for k,v in enumerate(nums):
            try:
                num2_index =  hash_table[target - v]
            except KeyError:
                hash_table[v] = k
            else:
                return (sorted([k,num2_index]))
 ''' used other ppl code as reference 
 their thought process: use another hashtable and add all num2_values and num2_indexes as key value pairs. then when encounter keyError, update the hash_table
 the else block is executed when there is an error besides KeyError, eg EOF(?) and returns the sorted answer.
 
 learnt: 
 you could use except blocks in place of if else statement. 
 
 time complexity: O(n)? since one 'for loop ' and enumerate function is O(1)
 '''
