"""
Two Sum II - Input Array Is Sorted

Given a 1-indexed array of integers numbers that is already sorted in
non-decreasing order, find two numbers such that they add up to a specific
target number.

Return the indices of the two numbers, index1 and index2, added by one as an
integer array [index1, index2] of length 2.

Constraints:
2 <= numbers.length <= 3 * 10^4
-1000 <= numbers[i] <= 1000
numbers is sorted in non-decreasing order.
-1000 <= target <= 1000
The tests are generated such that there is exactly one solution.
"""

import random
import time


def validate_input(numbers, target):
    if not isinstance(numbers, list):
        raise TypeError("numbers must be a list")
    if not isinstance(target, int):
        raise TypeError("target must be an integer")
    if not 2 <= len(numbers) <= 3 * 10**4:
        raise ValueError("numbers length must be between 2 and 30000")
    if not -1000 <= target <= 1000:
        raise ValueError("target must be between -1000 and 1000")

    previous = numbers[0]
    if not isinstance(previous, int):
        raise TypeError("numbers must contain only integers")
    if not -1000 <= previous <= 1000:
        raise ValueError("each number must be between -1000 and 1000")

    for value in numbers[1:]:
        if not isinstance(value, int):
            raise TypeError("numbers must contain only integers")
        if not -1000 <= value <= 1000:
            raise ValueError("each number must be between -1000 and 1000")
        if value < previous:
            raise ValueError("numbers must be sorted in non-decreasing order")
        previous = value


def two_sum(numbers, target):
    validate_input(numbers, target)

    left = 0
    right = len(numbers) - 1

    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        if total < target:
            left += 1
        else:
            right -= 1

    raise ValueError("no valid pair found")


def validate_solution(numbers, target, result):
    if not isinstance(result, list):
        return False, "result must be a list"
    if len(result) != 2:
        return False, "result must contain exactly two indices"

    index1, index2 = result
    if not isinstance(index1, int) or not isinstance(index2, int):
        return False, "indices must be integers"
    if not 1 <= index1 < index2 <= len(numbers):
        return False, "indices must satisfy 1 <= index1 < index2 <= len(numbers)"
    if numbers[index1 - 1] + numbers[index2 - 1] != target:
        return False, "selected indices do not add up to target"

    return True, "valid"


tests = [
    ([2, 7, 11, 15], 9, [1, 2]),
    ([2, 3, 4], 6, [1, 3]),
    ([-1, 0], -1, [1, 2]),
    ([-3, -1, 0, 2, 4, 8], 7, [2, 6]),
    ([1, 2, 3, 4, 4, 9], 8, [4, 5]),
    ([-10, -5, -2, 0, 1, 7, 11], 9, [3, 7]),
    ([0, 0, 3, 4], 0, [1, 2]),
    ([-1000, -999, 0, 999, 1000], 0, [1, 5]),
    ([1, 3], 4, [1, 2]),
    ([1, 2, 4, 6, 10, 14], 16, [2, 6]),
]


invalid_tests = [
    ([3, 2], 5, ValueError, "sorted"),
    ([1], 1, ValueError, "length"),
    ([0, 1001], 1001, ValueError, "between -1000 and 1000"),
    ([1, 2], 1001, ValueError, "target"),
    ([1, "2"], 3, TypeError, "integers"),
]


def run_basic_tests():
    for numbers, target, expected in tests:
        print(numbers, target, expected)
        start = time.perf_counter()
        ans = two_sum(numbers, target)
        end = time.perf_counter()

        is_valid, message = validate_solution(numbers, target, ans)
        passed = is_valid and ans == expected

        print(f"time={(end - start):.6f}s")
        print(True if passed else {"answer": ans, "validation": message})


def run_invalid_tests():
    print("\nInvalid input validation")
    for numbers, target, error_type, expected_message in invalid_tests:
        print(numbers, target, error_type.__name__)
        start = time.perf_counter()
        try:
            two_sum(numbers, target)
            result = False
        except Exception as exc:
            result = isinstance(exc, error_type) and expected_message in str(exc)
        end = time.perf_counter()

        print(f"time={(end - start):.6f}s")
        print(result)


def benchmark_growth():
    print("\nBenchmark for growth")
    previous_time = None
    for n in [10**2, 10**3, 10**4]:
        total_time = 0
        for _ in range(5):
            sample = sorted(random.randint(-1000, 1000) for _ in range(n))
            sample[0] = -1000
            sample[-1] = 1000
            start = time.perf_counter()
            two_sum(sample, 0)
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
    run_invalid_tests()
    benchmark_growth()
