#description 
#Given an integer array nums, 
# return true if any value appears at least twice in 
# the array, and return false if every element is distinct.
#Example 1:

#Input: nums = [1,2,3,1]

#Output: true

#Explanation:

#The element 1 occurs at the indices 0 and 3.


def containsDuplicate(nums):


        unique_nums = list(set(nums))


        return  len(unique_nums) != len(nums) 

#test
nums = [1,2,3,1]
print(containsDuplicate(nums))