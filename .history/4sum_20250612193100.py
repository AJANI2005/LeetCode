def fourSum(nums: list[int], target: int):

    for i in range(len(nums)):
        l,k = i + 1, len(nums) - 2
        h = len(nums) - 1

        while l < h:
            sum4 = nums[i] + nums[l] + nums[k] + nums[h]
            