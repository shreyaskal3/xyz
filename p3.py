"""
Squares of a Sorted Array
Easy
Topics
premium lock icon
Companies
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
 

Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?

"""
import random
import time


def squared(nums):
    n = len(nums)
    result = [0]*n
    left = 0
    right = n-1
    pos = n-1
    while left<=right:

        left_sq = nums[left]*nums[left]
        right_sq = nums[right]*nums[right]
        if left_sq > right_sq:
            result[pos] = left_sq
            left+=1
        else:
            result[pos] = right_sq
            right-=1
        pos -=1
    return result

tests = [
    ([-4,-1,0,3,10], [0,1,9,16,100]),
    ([-7,-3,2,3,11], [4,9,9,49,121]),
    ([0], [0]),
    ([1], [1]),
    ([-1], [1]),
    ([-2,-1], [1,4]),
    ([1,2,3], [1,4,9]),
    ([-3,-2,-1], [1,4,9]),
    ([-2,0,2], [0,4,4]),
    ([-5,-4,-3,-2,-1], [1,4,9,16,25]),
    ([0,0,0], [0,0,0]),
    ([-4,-1,0,0,3,10], [0,0,1,9,16,100]),
    ([-9,-7,-5,-3,-1], [1,9,25,49,81]),
    ([-10,-5,0,5,10], [0,25,25,100,100]),
    ([-10000,-9999,0,9999,10000], [0,99980001,99980001,100000000,100000000]),
]


for i,j in tests:
    print(i,j)
    start = time.perf_counter()
    ans = squared(i)
    end = time.perf_counter()

    print(f"time={(end-start):.6f}s")
    print(True if j==ans else ans)


print("\nBenchmark for growth")
previous_time = None
for n in [10**3, 10**4, 10**5]:
    total_time = 0
    for _ in range(5):
        sample = [random.randint(0, 10**4) for _ in range(n)]
        start = time.perf_counter()
        squared(sample)
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




