def fourSum(self, nums: list[int], target: int):
    nums.sort()
    n = len(nums)

    out = []
    for i in range(n):
        j = 0
        k = n - 1 
        while k > j:
            s = nums[i] + nums[j] + nums[k]
            if s == target:
                out.append([nums[i],nums[j],nums[k]])
            elif s < target: 
                k -= 1


        