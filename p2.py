"""

Container With Most Water

Given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the `i-th` line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container holds the maximum amount of water.

Return the maximum amount of water a container can store.

Note:
You may not slant the container.

Example 1

Input: height = [1,8,6,2,5,4,8,3,7 ]
Output: 49
Explanation:
The maximum area is formed by the lines at index 1 and index 8.

Example 2

Input: height = [1,1]
Output: 1

Constraints

2 <= height.length <= 10^5
0 <= height[i] <= 10^4

(0,0) (0,1)
(1,0) (1,8)
 (2,0) (2,6)
"""
import random
import time


height = [1,8,6,2,5,4,8,3,7 ] 
def container(height):
    area = 0
    n = len(height)
    best_left,best_right = 0,n-1
    
    left = 0
    right = n-1
    while left<right:

        now = (right - left)*min(height[left],height[right])
        if area< now:
            area = now
            best_left,best_right = left,right

        if height[left]<height[right]:
            left+=1
        else:
            right-=1

        
    return (best_right-best_left) * min(height[best_left],height[best_right])

tests = [
    # ([1, 1], 1),
    # ([1, 2, 1], 2),
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([4, 3, 2, 1, 4], 16),
    ([1, 2, 4, 3], 4),
    ([5, 4, 3, 2, 1], 6),
    ([1, 2, 3, 4, 5], 6),
    ([0, 2, 0, 4, 0], 4),
    ([10000, 0, 10000], 20000),
    ([2, 3, 10, 5, 7, 8, 9], 36),
    ([0,0],0),
    ([5,5,5,5],15),
    ([0,1,0,1],2),
    ([1,2,0],1)
]


for i,j in tests:
    print(i,j)
    start = time.perf_counter()
    ans = container(i)
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
        container(sample)
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
