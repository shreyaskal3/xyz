"""

Remove Duplicates from Sorted Array


Problem


Hints
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return _the number of unique elements in _nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length; for (int i = 0; i < k; i++) { assert nums[i] == expectedNums[i]; }

If all assertions pass, then your solution will be accepted.

 

Example 1:

Input: nums = [1,1,2] Output: 2, nums = [1,2,_] Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively. It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4] Output: 5, nums = [0,1,2,3,4,,,,,_] Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively. It does not matter what you leave beyond the returned k (hence they are underscores).

 

Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
Need help or want more practice?




"""

import time


def remove_duplicates(nums):
    val = None
    unique = 0
    left ,right = 0,len(nums)-1
    while left <right:
        if not val:
            val = i
            unique+=1
        if val==i:
            # nums.pop(index)
        if val!=i:
            val = i
            unique+=1
    print("unique ",unique,nums)
    return unique
        


    raise NotImplementedError("Implement remove_duplicates(nums) before running tests")


def validate_result(original_nums, mutated_nums, k, expected_k, expected_nums):
    if k != expected_k:
        return False, f"expected k={expected_k}, got {k}"

    if mutated_nums[:k] != expected_nums[:k]:
        return (
            False,
            f"expected first {k} values to match {expected_nums[:k]}, got {mutated_nums[:k]}",
        )

    if len(original_nums) != len(mutated_nums):
        return False, "array length changed"

    return True, "valid"


tests = [
    ([1, 1, 2], 2, [1, 2]),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
    ([1], 1, [1]),
    ([1, 1, 1, 1], 1, [1]),
    ([1, 2, 3, 4], 4, [1, 2, 3, 4]),
    ([1, 1, 2, 2, 3, 3], 3, [1, 2, 3]),
    ([-3, -3, -2, -2, -1, -1], 3, [-3, -2, -1]),
    ([0, 0, 0, 0, 0], 1, [0]),
    ([-100, -100, 0, 0, 100, 100], 3, [-100, 0, 100]),
    ([1, 2, 2, 2, 3, 4, 4, 5], 5, [1, 2, 3, 4, 5]),
]


def run_basic_tests():
    for nums, expected_k, expected_nums in tests:
        original = nums[:]
        print(f"nums={original}")
        start = time.perf_counter()
        k = remove_duplicates(nums)
        end = time.perf_counter()

        is_valid, message = validate_result(
            original, nums, k, expected_k, expected_nums
        )

        print(f"time={(end - start):.6f}s")
        print(True if is_valid else {"k": k, "nums": nums, "error": message})


if __name__ == "__main__":
    try:
        run_basic_tests()
    except NotImplementedError as exc:
        print(exc)


