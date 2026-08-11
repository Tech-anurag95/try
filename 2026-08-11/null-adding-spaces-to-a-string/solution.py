1class Solution:
2    def addSpaces(self, s: str, spaces: List[int]) -> str:
3        ans=[]
4        j=0
5        for i in range(len(s)):
6            if j < len(spaces) and i==spaces[j]:
7                ans.append(" ")
8                j+=1
9            ans.append(s[i])
10        return "".join(ans)