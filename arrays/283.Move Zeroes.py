#description
#Given an integer array nums, move all 0's to the 
# end of it while maintaining the relative order
#  of the non-zero elements.

#Note that you must do this in-place without making a copy of the array.

#Example 1:
#Input: nums = [0,1,0,3,12]
#Output: [1,3,12,0,0]
def moveZeroes(nums):
        
        count = 0
        for i in reversed(nums):
            if i == 0:
                nums.remove(i)
                count += 1
        nums += [0] * count
        return nums