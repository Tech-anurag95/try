1class Solution:
2    def findKthLargest(self, nums: List[int], k: int) -> int:
3        nums.sort()
4        return nums[len(nums)-k]
5