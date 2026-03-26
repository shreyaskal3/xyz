"""
3Sum
Medium
Topics
premium lock icon
Companies
Hint
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105

"""

import random
import time

def triplets(nums):
    nums = sorted(nums)
    n = len(nums)
    result = []

    for i in range(n - 2):
        if i>0 and nums[i]==nums[i-1]:
            continue
        left = i
        right = n-1

        while left<right:
            total = nums[i]+nums[left]+nums[right]

            if total == 0:
                result.append([nums[i],nums[left],nums[right]])
                
                while left<right and nums[left]==nums[left+1]:
                    left+=1
                while left<right and nums[right]==nums[right-1]:
                    right-=1

                left+=1
                right-=1
            if total<0:
                left+=1
            if total>0:
                right-=1
    return result


def normalize_triplets(values):
    return sorted(sorted(item) for item in values)


tests = [
    ([-1,0,1,2,-1,-4], [[-1,-1,2],[-1,0,1]]),
    ([0,1,1], []),
    ([0,0,0], [[0,0,0]]),
    ([0,0,0,0], [[0,0,0]]),
    ([-2,0,0,2,2], [[-2,0,2]]),
    ([-2,0,1,1,2], [[-2,0,2],[-2,1,1]]),
    ([-1,0,1,0], [[-1,0,1]]),
    ([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6], [[-4,-2,6],[-4,0,4],[-4,1,3],[-4,2,2],[-2,-2,4],[-2,0,2]]),
    ([-5,-4,-3,-2,-1], []),
    ([1,2,3,4,5], []),
    ([-1,-1,-1,2,2], [[-1,-1,2]]),
    ([-3,0,1,2,-1,1,-2], [[-3,1,2],[-2,0,2],[-2,1,1],[-1,0,1]]),
]


for i,j in tests:
    print(i,j)
    start = time.perf_counter()
    ans = triplets(i)
    end = time.perf_counter()

    print(f"time={(end-start):.6f}s")
    print(True if normalize_triplets(j) == normalize_triplets(ans) else ans)


print("\nBenchmark for growth")
previous_time = None
for n in [10**2, 3 * 10**2, 10**3]:
    total_time = 0
    for _ in range(5):
        sample = [random.randint(0, 10**4) for _ in range(n)]
        start = time.perf_counter()
        triplets(sample)
        end = time.perf_counter()
        total_time += end - start

    avg_time = total_time / 5
    if previous_time is None:
        print(f"n={n}, avg_time={avg_time:.6f}s")
    else:
        print(
            f"n={n}, avg_time={avg_time:.6f}s, "
            f"growth_vs_prev={avg_time / previous_time:.2f}x"
        )
    previous_time = avg_time



