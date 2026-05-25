#description
#Given an array nums. We define a running sum of 
# n array as runningSum[i] = sum(nums[0]…nums[i]).

#Return the running sum of nums.

#Example 1:

#Input: nums = [1,2,3,4]
#Output: [1,3,6,10]
#Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].


def runningSum(nums):
        
        current_sum = 0
        empty = []
        for i in range(len(nums)):
            empty.append(current_sum + nums[i])
            current_sum += nums[i]
        return empty