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