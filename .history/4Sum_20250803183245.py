def fourSum(self, nums: list[int], target: int):
    nums.sort()
    n = len(nums)
    for i in range(n):
        j = 0
        k = n - 1
        