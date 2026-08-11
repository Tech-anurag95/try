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