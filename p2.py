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
import multiprocessing as mp
import tracemalloc


TIME_LIMIT_S = 0.10
SPACE_LIMIT_MB = 32.0
PROCESS_STARTUP_GRACE_S = 2


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


def _limit_worker(arr, q):
    try:
        tracemalloc.start()
        start = time.perf_counter()
        ans = container(arr)
        elapsed = time.perf_counter() - start
        _, peak_bytes = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        q.put(("OK", ans, elapsed, peak_bytes / (1024 * 1024)))
    except Exception as exc:
        q.put(("RTE", str(exc), None, None))


def run_with_limits(arr, time_limit_s=TIME_LIMIT_S, space_limit_mb=SPACE_LIMIT_MB):
    q = mp.Queue()
    process = mp.Process(target=_limit_worker, args=(arr, q))
    process.start()
    process.join(time_limit_s + PROCESS_STARTUP_GRACE_S)

    if process.is_alive():
        process.terminate()
        process.join()
        return "TLE", None, None, None

    if q.empty():
        return "RTE", None, None, None

    status, payload, elapsed, peak_mb = q.get()
    if status != "OK":
        return status, payload, elapsed, peak_mb

    if elapsed is not None and elapsed > time_limit_s:
        return "TLE", payload, elapsed, peak_mb

    if peak_mb is not None and peak_mb > space_limit_mb:
        return "MLE", payload, elapsed, peak_mb

    return "OK", payload, elapsed, peak_mb

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


def run_basic_tests():
    print(
        f"Judge limits: time={TIME_LIMIT_S:.3f}s, "
        f"space={SPACE_LIMIT_MB:.1f}MB\n"
    )
    for arr, expected in tests:
        print(arr, expected)
        status, ans, elapsed, peak_mb = run_with_limits(arr)
        print(
            f"status={status}, time={elapsed:.6f}s, peak_mem={peak_mb:.4f}MB"
            if elapsed is not None and peak_mb is not None
            else f"status={status}"
        )
        print(True if status == "OK" and ans == expected else ans)


def benchmark_growth():
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


if __name__ == "__main__":
    run_basic_tests()
    benchmark_growth()
