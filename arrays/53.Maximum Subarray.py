#description
#Given an integer array nums, find the subarray with the largest sum, 
# and return its sum.

 #Example :

#Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
#Output: 6
#Explanation: The subarray [4,-1,2,1] has the largest sum 6.
def maxSubArray(self, nums):
        
        current_max = nums[0]
        global_max = nums[0]
    
        for i in range(1, len(nums)):
        
            current_max = max(nums[i], current_max + nums[i])
        
        
            if current_max > global_max:
                global_max = current_max
            
        return global_max