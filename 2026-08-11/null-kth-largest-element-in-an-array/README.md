# null. Kth Largest Element In An Array

| Field | Value |
|---|---|
| **Date** | 2026-08-11 |
| **Time** | 2026-08-11T14:20:05.810Z |
| **Difficulty** | Easy |
| **Topics** | Array, Divide and Conquer, Sorting, Heap (Priority Queue), Quickselect |
| **Language** | python3 |
| **Runtime** | 58 ms |
| **Memory** | 31.1 MB |

## Problem Description

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

Can you solve it without sorting?

 
Example 1:
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5
Example 2:
Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4

 
Constraints:


	1 <= k <= nums.length <= 105
	-104 <= nums[i] <= 104

## Solution

```python3
1class Solution:
2    def findKthLargest(self, nums: List[int], k: int) -> int:
3        nums.sort()
4        return nums[len(nums)-k]
5
```
