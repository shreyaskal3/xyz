"""

Two Sum
Subscribe to TUF+

Hints
Company
Given an array of integers nums and an integer target. Return the indices(0 - indexed) of two elements in nums such that they add up to target.



Each input will have exactly one solution, and the same element cannot be used twice. Return the answer in increasing order.


Example 1

Input: nums = [1, 6, 2, 10, 3], target = 7

Output: [0, 1]

Explanation:

nums[0] + nums[1] = 1 + 6 = 7

Example 2

Input: nums = [1, 3, 5, -7, 6, -3], target = 0

Output: [1, 5]

Explanation:

nums[1] + nums[5] = 3 + (-3) = 0

Now your turn!

Input: nums = [-6, 7, 1, -7, 6, 2], target = 3

Output:

Pick your answer


[0, 1]

[3, 6]

[1, 2]

[2, 5]
Constraints

2 <= nums.length <= 105
-104 <= nums[i] <= 104
-105 <= target <= 105
Only one valid answer exists.


"""

class Solution:
    def main(self,nums,target):
        result = []
        for i,ele in enumerate(nums):
            for j,ele1 in enumerate(nums[i+1:]):
                if target==ele+ele1:
                    result.extend([i,i+j+1])
        return result
    # TC O(N2)
    # SC O(1)
    def second(self,nums,target):
        result = []
        for i,ele in enumerate(nums):
            for j,ele1 in enumerate(nums[i+1:]):
                if target==ele+ele1:
                    result.extend([i,i+j+1])
        return result

print(Solution().main([-6, 7, 1, -7, 6, 2],3)) #[2, 5]
print(Solution().main([1, 6, 2, 10, 3], 7)) #[0, 1]
print(Solution().main([1, 3, 5, -7, 6, -3],0)) #[1, 5]
