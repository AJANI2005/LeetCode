def fourSum(nums: list[int], target: int):

    nums.sort()
    for i in range(len(nums)):

        l,h = i,len(nums)-1
        l2,h2 = l + 1, h - 1

        while l2 < h2:
            sum4 = nums[l] +  nums[l2] + nums[h] + nums[h2]



