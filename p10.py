"""

Move Pieces to Obtain a String
Difficulty: Medium

Category: DSA

Topics: Two Pointers, String

You are given two strings `start` and `target`, both of length `n`. Each string consists **only** of the characters `'L'`, `'R'`, and `'_'` where: - The characters `'L'` and `'R'` represent pieces, where a piece `'L'` can move to the **left** only if there is a **blank** space directly to its left, and a piece `'R'` can move to the **right** only if there is a **blank** space directly to its right. - The character `'_'` represents a blank space that can be occupied by **any** of the `'L'` or `'R'` pieces. Return `true` _if it is possible to obtain the string_ `target`_ by moving the pieces of the string _`start`_ **any** number of times_. Otherwise, return `false`.   **Example 1:** **Input:** start = "_L__R__R_", target = "L______RR" **Output:** true **Explanation:** We can obtain the string target from start by doing the following moves: - Move the first piece one step to the left, start becomes equal to "**L**___R__R_". - Move the last piece one step to the right, start becomes equal to "L___R___**R**". - Move the second piece three steps to the right, start becomes equal to "L______**R**R". Since it is possible to get the string target from start, we return true. ``` **Example 2:** **Input:** start = "R_L_", target = "__LR" **Output:** false **Explanation:** The 'R' piece in the string start can move one step to the right to obtain "_**R**L_". After that, no pieces can move anymore, so it is impossible to obtain the string target from start. ``` **Example 3:** **Input:** start = "_R", target = "R_" **Output:** false **Explanation:** The piece in the string start can move only to the right, so it is impossible to obtain the string target from start. ```   **Constraints:** - `n == start.length == target.length` - `1 <= n <= 105` - `start` and `target` consist of the characters `'L'`, `'R'`, and `'_'`.
Editorial


Problem

Solution

History
Move Pieces to Obtain a String
Medium
DSA
Topics:
Two Pointers
String

Description

Test Cases

Hints
You are given two strings start and target, both of length n. Each string consists only of the characters 'L', 'R', and '_' where:

The characters 'L' and 'R' represent pieces, where a piece 'L' can move to the left only if there is a blank space directly to its left, and a piece 'R' can move to the right only if there is a blank space directly to its right.
The character '_' represents a blank space that can be occupied by any of the 'L' or 'R' pieces.
Return true if it is possible to obtain the string target_ by moving the pieces of the string start any number of times_. Otherwise, return false.

 

Example 1:

Input: start = "L__R__R", target = "L______RR" Output: true Explanation: We can obtain the string target from start by doing the following moves:

Move the first piece one step to the left, start becomes equal to "L__R__R".
Move the last piece one step to the right, start becomes equal to "L___R___R".
Move the second piece three steps to the right, start becomes equal to "L______RR". Since it is possible to get the string target from start, we return true.
Example 2:

Input: start = "R_L_", target = "__LR" Output: false Explanation: The 'R' piece in the string start can move one step to the right to obtain "RL". After that, no pieces can move anymore, so it is impossible to obtain the string target from start.

Example 3:

Input: start = "R", target = "R" Output: false Explanation: The piece in the string start can move only to the right, so it is impossible to obtain the string target from start.

Constraints:

n == start.length == target.length
1 <= n <= 105
start and target consist of the characters 'L', 'R', and '_'.
Need help or want more practice?

Get AI Coach help

Try random interview
1:16:34
0% used
AI Code Feedback: 0







"""

import time


def can_change(start, target):
    n = len(start)
    i,j=0,0
    while i<n and j<n:
        while i < n and start[i]=="_":
            i+=1
        while j<n and target[j]=="_":
            j+=1
        if i==n or j==n:
            return i==n and j==n
        
        if start[i] != target[j]:
            return False
        
        if start[i]=="L" and i <j:
            return False
        if start[i]=="R" and i>j:
            return False
        i+=1
        j+=1
    return True
    # raise NotImplementedError("Implement can_change(start, target) before running tests")


def validate_result(result, expected):
    if not isinstance(result, bool):
        return False, f"expected return type bool, got {type(result).__name__}"

    if result != expected:
        return False, f"expected {expected}, got {result}"

    return True, "valid"


tests = [
    ("R__L", "_RL_", False),
    ("_L__R__R_", "L______RR", True),
    ("R_L_", "__LR", False),
    ("_R", "R_", False),
    ("L_", "_L", False),
    ("_L", "L_", True),
    ("R_", "_R", True),
    ("___", "___", True),
    ("_R_L_", "__RL_", True),
    ("__L__R__", "L_____R_", True),
    
    ("_L_R__", "L___R_", True),
    ("_R__L_", "__R_L_", True),
]


def run_basic_tests():
    for start_str, target_str, expected in tests:
        print(f"start={start_str}, target={target_str}")
        begin = time.perf_counter()
        result = can_change(start_str, target_str)
        end = time.perf_counter()

        is_valid, message = validate_result(result, expected)

        print(f"time={(end - begin):.6f}s")
        print(True if is_valid else {"result": result, "error": message})


if __name__ == "__main__":
    try:
        run_basic_tests()
    except NotImplementedError as exc:
        print(exc)

