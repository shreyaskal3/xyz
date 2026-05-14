"""

Remove Duplicates from Sorted Array II
Difficulty: Medium

Given an integer array `nums` sorted in **non-decreasing order**, remove some duplicates **in-place** such that each unique element appears **at most twice**. The **relative order** of the elements should be kept the **same**. Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the **first part** of the array `nums`. More formally, if there are `k` elements after removing the duplicates, then the first `k` elements of `nums` should hold the final result. It does not matter what you leave beyond the first `k` elements. Return `k`_ after placing the final result in the first _`k`_ slots of _`nums`. Do **not** allocate extra space for another array. You must do this by **modifying the input array in-place** with O(1) extra memory. **Custom Judge:** The judge will test your solution with the following code: int[] nums = [...]; // Input array int[] expectedNums = [...]; // The expected answer with correct length int k = removeDuplicates(nums); // Calls your implementation assert k == expectedNums.length; for (int i = 0; i < k; i++) { assert nums[i] == expectedNums[i]; } ``` If all assertions pass, then your solution will be **accepted**.   **Example 1:** **Input:** nums = [1,1,1,2,2,3] **Output:** 5, nums = [1,1,2,2,3,_] **Explanation:** Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively. It does not matter what you leave beyond the returned k (hence they are underscores). ``` **Example 2:** **Input:** nums = [0,0,1,1,1,1,2,3,3] **Output:** 7, nums = [0,0,1,1,2,3,3,_,_] **Explanation:** Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively. It does not matter what you leave beyond the returned k (hence they are underscores). ```   **Constraints:** - `1 <= nums.length <= 3 * 104` - `-104 <= nums[i] <= 104` - `nums` is sorted in **non-decreasing** order.
Editorial

Problem

Solution

History
Remove Duplicates from Sorted Array II
Medium
DSA
Topics:
Array
Two Pointers

Description

Test Cases

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k_ after placing the final result in the first k slots of _nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length; for (int i = 0; i < k; i++) { assert nums[i] == expectedNums[i]; }

If all assertions pass, then your solution will be accepted.


Example 1:

Input: nums = [1,1,1,2,2,3] Output: 5, nums = [1,1,2,2,3,_] Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively. It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,0,1,1,1,1,2,3,3] Output: 7, nums = [0,0,1,1,2,3,3,,] Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively. It does not matter what you leave beyond the returned k (hence they are underscores).

 

Constraints:

1 <= nums.length <= 3 * 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.
Need help or want more practice?




"""

import time


def remove_duplicates(nums):
    if len(nums) <= 2:
        return len(nums), nums[:]

    write = 2

    for read in range(2, len(nums)):
        if nums[read] != nums[write - 2]:
            nums[write] = nums[read]
            write += 1

    return write, nums[:write]

    raise NotImplementedError("Implement remove_duplicates(nums) before running tests")


def validate_result(original_nums, mutated_nums, result, expected_k, expected_nums):
    returned_nums = None
    k = result

    if isinstance(result, tuple):
        if len(result) != 2:
            return False, "expected tuple return as (k, nums_prefix)"
        k, returned_nums = result

    if not isinstance(k, int):
        return False, f"expected return type int for k, got {type(k).__name__}"

    if k != expected_k:
        return False, f"expected k={expected_k}, got {k}"

    if returned_nums is not None:
        if not isinstance(returned_nums, list):
            return False, "expected returned nums prefix to be a list"
        if returned_nums != expected_nums[:k]:
            return (
                False,
                f"expected returned nums prefix {expected_nums[:k]}, got {returned_nums}",
            )

    if mutated_nums[:k] != expected_nums[:k]:
        return (
            False,
            f"expected first {k} values to match {expected_nums[:k]}, got {mutated_nums[:k]}",
        )

    if len(original_nums) != len(mutated_nums):
        return False, "array length changed"

    for index in range(2, k):
        if mutated_nums[index] == mutated_nums[index - 1] == mutated_nums[index - 2]:
            return False, "found a value more than twice in the kept prefix"

    return True, "valid"


tests = [
    ([1, 1, 1, 2, 2, 3], 5, [1, 1, 2, 2, 3]),
    ([0, 0, 1, 1, 1, 1, 2, 3, 3], 7, [0, 0, 1, 1, 2, 3, 3]),
    ([1], 1, [1]),
    ([1, 1], 2, [1, 1]),
    ([1, 1, 1], 2, [1, 1]),
    ([1, 2, 3, 4], 4, [1, 2, 3, 4]),
    ([1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4], 8, [1, 1, 2, 2, 3, 3, 4, 4]),
    ([-1, -1, -1, 0, 0, 0, 1, 1, 1], 6, [-1, -1, 0, 0, 1, 1]),
    ([5, 5, 5, 5, 5], 2, [5, 5]),
    ([-10000, -10000, -10000, 10000, 10000, 10000], 4, [-10000, -10000, 10000, 10000]),
    ([1, 1, 1, 2, 2, 2, 3, 3], 6, [1, 1, 2, 2, 3, 3]),
    ([0, 0, 0, 1, 1, 1, 2, 2, 2], 6, [0, 0, 1, 1, 2, 2]),
]


def run_basic_tests():
    for nums, expected_k, expected_nums in tests:
        original = nums[:]
        print(f"nums={original}")
        start = time.perf_counter()
        result = remove_duplicates(nums)
        end = time.perf_counter()

        is_valid, message = validate_result(
            original, nums, result, expected_k, expected_nums
        )

        print(f"time={(end - start):.6f}s")
        print(True if is_valid else {"result": result, "nums": nums, "error": message})


if __name__ == "__main__":
    try:
        run_basic_tests()
    except NotImplementedError as exc:
        print(exc)
