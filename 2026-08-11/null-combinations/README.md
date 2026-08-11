# null. Combinations

| Field | Value |
|---|---|
| **Date** | 2026-08-11 |
| **Time** | 2026-08-11T16:33:56.130Z |
| **Difficulty** | Medium |
| **Topics** | Backtracking |
| **Language** | python3 |
| **Runtime** | 110 ms |
| **Memory** | 61.3 MB |

## Problem Description

Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.

 
Example 1:

Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.


Example 2:

Input: n = 1, k = 1
Output: [[1]]
Explanation: There is 1 choose 1 = 1 total combination.


 
Constraints:


	1 <= n <= 20
	1 <= k <= n

## Solution

```python3
1class Solution:
2    def combine(self, n: int, k: int) -> List[List[int]]:
3        ans = []
4
5        def backtrack(start, path):
6            if len(path) == k:
7                ans.append(path.copy())
8                return
9
10            for i in range(start, n + 1):
11                path.append(i)          # choose
12                backtrack(i + 1, path)  # explore
13                path.pop()               # undo
14
15        backtrack(1, [])
16        return ans
```
