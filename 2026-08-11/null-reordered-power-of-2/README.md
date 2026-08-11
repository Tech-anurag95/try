# null. Reordered Power Of 2

| Field | Value |
|---|---|
| **Date** | 2026-08-11 |
| **Time** | 2026-08-11T17:38:12.758Z |
| **Difficulty** | Medium |
| **Topics** | Hash Table, Math, Sorting, Counting, Enumeration |
| **Language** | python3 |
| **Runtime** | 6 ms |
| **Memory** | 19.2 MB |

## Problem Description

You are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this so that the resulting number is a power of two.

 
Example 1:

Input: n = 1
Output: true


Example 2:

Input: n = 10
Output: false


 
Constraints:


	1 <= n <= 109

## Solution

```python3
1class Solution:
2    def reorderedPowerOf2(self, n: int) -> bool:
3        from collections import Counter
4        dic=Counter(str(n))
5        i=0
6        while len(str(2**i))<=len(str(n)):
7            if Counter(str(2**i))==dic:
8                return True
9            i+=1
10        return False
```
